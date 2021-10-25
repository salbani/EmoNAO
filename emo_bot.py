
from fer import FER
import cv2

from keyframes import hello, sad, handsUp, handsDown

from angle_interpolation import AngleInterpolationAgent

class EmoBotAgent(AngleInterpolationAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(EmoBotAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        
        self.isAngry = False
        self.cap = cv2.VideoCapture(0)

        # Check if the webcam is opened correctly
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

        self.detector = FER()
        
    def think(self, perception):
        if  not self.is_animating():
            ret, frame = self.cap.read()
            frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

            emotion, score = self.detector.top_emotion(frame)
            print(emotion, score)
            
            if self.isAngry == True and (emotion != 'angry' or score == None or score < 0.6):
                print("not angry")
                self.start_animation(handsDown())
                self.isAngry = False

            elif emotion == 'angry' and score > 0.6 and self.isAngry == False:
                print("angry")
                self.start_animation(handsUp())
                self.isAngry = True

            elif emotion == 'happy' and score > 0.8:
                print("wave")
                self.start_animation(hello())
            
            elif emotion == 'sad' and score > 0.6:
                print("sad")
                self.start_animation(sad())

        return super(EmoBotAgent, self).think(perception)
    
if __name__ == '__main__':
    agent = EmoBotAgent()     
    agent.run()