from pid import PIDAgent
from scipy import interpolate

class AngleInterpolationAgent(PIDAgent):
    def __init__(self, simspark_ip='localhost',
                 simspark_port=3100,
                 teamname='DAInamite',
                 player_id=0,
                 sync_mode=True):
        super(AngleInterpolationAgent, self).__init__(simspark_ip, simspark_port, teamname, player_id, sync_mode)
        self.keyframes = ([], [], [])

    def think(self, perception):
        target_joints = self.angle_interpolation(self.keyframes, perception)
        self.target_joints.update(target_joints)
        return super(AngleInterpolationAgent, self).think(perception)

    def start_animation(self, keyframes):
        self.start_time = -1
        self.keyframes = keyframes
        joint_angles = list(map(lambda joint : list(map(lambda key : key[0], joint)), self.keyframes[2]))
        ks = list(map(lambda times : min([3, len(times)-1-(len(times)%2)]), keyframes[1]))       
        self.splines = list(map(lambda times, angles, k : interpolate.splrep(times, angles, s=0, k=k), self.keyframes[1], joint_angles, ks))
        print('started animation')

    def stop_animation(self):
        del self.start_time
        self.keyframes = ([],[],[])
        print('stopped animation')

    def is_animating(self):
        return hasattr(self, 'start_time')

    def angle_interpolation(self, keyframes, perception):
        if not self.is_animating():
            return {}

        if self.start_time == -1:
            self.start_time = perception.time

        time = perception.time - self.start_time
            
        finished_keyframes = list(map(lambda times : times[-1] < time, keyframes[1]))

        last_angles = list(map(lambda keys : keys[-1][0], keyframes[2]))
        target_angles = list(map(lambda spline, finished, last_angle : interpolate.splev([time], spline)[0] if not finished else last_angle, self.splines, finished_keyframes, last_angles))

        if all(finished_keyframes):
            self.stop_animation()

        target_joints = dict(zip(keyframes[0], target_angles))
        
        if "LHipYawPitch" in target_joints:
            target_joints["RHipYawPitch"] = target_joints["LHipYawPitch"]
            
        return target_joints
