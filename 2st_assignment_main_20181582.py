from SEN040134 import SEN040134_Tracking as Tracking_Sensor
# import Tracking sensor module(time module included)
import time
import RPi.GPIO as GPIO
import rear_wheels
import front_wheels


def drive_parking(self):
    # front wheels center allignment
    self.front_steering.turn_straight()

    # power down both wheels
    self.rear_wheels_drive.stop()
    self.rear_wheels_drive.power_down()

if __name__ == "__main__":
    Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])
    a = [55, 60, 80, 85, 95, 100, 120, 125]
    b = [30, 40, 50] # 0 = 30, 1 = 50
    direction_controller = front_wheels.Front_Wheels(db='config')
    driving_controller = rear_wheels.Rear_Wheels(db='config')
    
    try:
        while True:
            print("현재 탐지 결과입니다 : ", Tracker.read_digital())
            print("구동체가 라인을 감지한 결과는 : ", Tracker.is_in_line())
            print("라인 중앙을 감지한 결과는 : ", Tracker.is_center())
            time.sleep(1)

            if Tracker.is_equal_status([1,0,0,0,0]):
                direction_controller.turn(a[0])
                driving_controller.forward_with_speed(b[0])

            elif Tracker.is_equal_status([1,1,0,0,0]):
                direction_controller.turn(a[1])
                driving_controller.forward_with_speed(b[0])

            elif Tracker.is_equal_status([0,1,0,0,0]):
                direction_controller.turn(a[2])
                driving_controller.forward_with_speed(b[0])

            elif Tracker.is_equal_status([0,1,1,0,0]):
                direction_controller.turn(a[3])
                driving_controller.forward_with_speed(b[1])

            elif Tracker.is_equal_status([0,0,1,0,0]):
                direction_controller.turn(90) # Go
                driving_controller.forward_with_speed(b[2])

            elif Tracker.is_equal_status([0,0,1,1,0]):
                direction_controller.turn(a[4])
                driving_controller.forward_with_speed(b[1])

            elif Tracker.is_equal_status([0,0,0,1,0]):
                direction_controller.turn(a[5])
                driving_controller.forward_with_speed(b[0])
                
            elif Tracker.is_equal_status([0,0,0,1,1]):
                direction_controller.turn(a[6])
                driving_controller.forward_with_speed(b[0])

            elif Tracker.is_equal_status([0,0,0,0,1]):
                direction_controller.turn(a[7])
                driving_controller.forward_with_speed(b[0])

            elif Tracker.is_in_line() == False: # Not Line -> [0,0,0,0,0]
                # Back
                driving_controller.backward_with_speed(b[0])

            else: # 혹시 모를 오류
                try:
                    print("Error!")
                    print(Tracker.read_digital())
                    #break
                except:
                    print("Error!!!!!!!!!!!!!")
                    print(Tracker.read_digital())
                    break

            '''

            
            # Second [0,0,0,0,0] Such and Turn
            # [1,?,0,0,0] -> 30 right
            if Tracker.read_digital()[0] == 1:
                # [1,1,0,0,0]
                if Tracker.read_digital()[1] == 1 and Tracker.is_center == False:
                    direction_controller.turn(a[6])
                    #direction_controller.turn_right()
                    driving_controller.forward_with_speed(b[0])
                # [1,0,0,0,0] -> 35 right
                elif Tracker.read_digital()[1] == 0:
                    direction_controller.turn(a[7])
                    ##direction_controller.turn_right()
                    driving_controller.forward_with_speed(b[0])
            # [0,1,0,0,0]        
            elif Tracker.read_digital()[1] == 1 and Tracker.is_center == False:
                direction_controller.turn(a[5])
                ##direction_controller.turn_right()
                driving_controller.forward_with_speed(b[0])

            # [0,?,1,?,0]
            elif Tracker.is_center() == True: # [?,?,1,?,?]
                # [?,1,1,0,?] -> 5 right
                if Tracker.read_digital()[1] == 1 and Tracker.read_digital()[3] == 0:
                    direction_controller.turn(a[4])
                    ##direction_controller.turn_right()
                    driving_controller.forward_with_speed(b[1])
                # [?,0,1,1,?] -> 5 left
                elif Tracker.read_digital()[1] == 0 and Tracker.read_digital()[3] == 1:
                    direction_controller.turn(a[3])
                    ##direction_controller.turn_left()
                    driving_controller.forward_with_speed(b[1])
                #[0,0,1,0,0]
                elif Tracker.read_digital()[1] == 0 and Tracker.read_digital()[3] == 0:
                    direction_controller.turn_straight()
                    driving_controller.forward_with_speed(b[1])

            # [?,?,?,1,?] -> 10 left
            elif Tracker.read_digital()[3] == 1:
                # [?,?,0,1,0] -> 10 left
                if Tracker.is_center() == False and Tracker.read_digital()[4] == 0:
                    direction_controller.turn(a[2])
                    ##direction_controller.turn_left()
                    driving_controller.forward_with_speed(b[0])
                # [?,?,0,1,1] -> 30 left
                elif Tracker.is_center() == False and Tracker.read_digital()[4] == 1:
                    direction_controller.turn(a[1])
                    ##direction_controller.turn_left()
                    driving_controller.forward_with_speed(b[0])
            # [?,?,?,0,1] -> 35 left
            elif Tracker.read_digital()[4] == 1:
                direction_controller.turn(a[0])
                ##direction_controller.turn_left()
                driving_controller.forward_with_speed(b[0])


            elif Tracker.is_in_line() == False: # Not Line -> [0,0,0,0,0]
                # Back
                driving_controller.backward_with_speed(b[0])

            else: # 혹시 모를 오류
                try:
                    print("Error!")
                    print(Tracker.read_digital())
                    #break
                except:
                    print("Error!!!!!!!!!!!!!")
                    print(Tracker.read_digital())
                    break
                    '''

            # Turn speed -> 30, Go speed -> 50
            # Little Turn speed -> 50!
            
            
            
    except KeyboardInterrupt:
        GPIO.cleanup()
