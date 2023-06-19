import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 
import requests

class ImageSubscriber(Node):

  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(Image, 'video_frames', self.listener_callback, 10)
    self.br = CvBridge()

  def listener_callback(self, data):
    self.get_logger().info('Receiving video frame')
    current_frame = self.br.imgmsg_to_cv2(data)
    _, img_encoded = cv2.imencode('.png', current_frame)
    frame_data = img_encoded.tobytes()
    url = "http://127.0.0.1:3000/upload"
    files=[
      ('content',('lala.png',frame_data,'image/png'))
    ]
    response = requests.request("POST", url, files=files)
    if response.status_code == 200:
        print('Frame sent successfully!')
    else:
        print('Failed to send frame. Status code:', response.status_code)
        
    cv2.imshow("Camera", current_frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      return
    
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()