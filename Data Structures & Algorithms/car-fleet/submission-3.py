class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        time = None
        fleet = dict(zip(position, speed))
        position = sorted(position, reverse=True)

        for pos in position:
            pos_time = (target - pos) / fleet[pos]
            if time is None:
                fleet_count += 1
                time = pos_time
            else:
                if pos_time > time:
                    fleet_count += 1
                    time = pos_time
            

        return fleet_count

                
