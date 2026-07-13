class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        cars = sorted(zip(position, speed), key=lambda x: -x[0])

        unobstructed_time = [(target - p) / s for p, s in cars]

        i = 1

        num_fleets = 1

        print(f"cars {cars}")
        print(f"unobstructed_time {unobstructed_time}")

        while i < len(cars):
            if unobstructed_time[i] > unobstructed_time[i-1]:
                # will not catch up, new fleet
                num_fleets += 1
            else:
                unobstructed_time[i] = unobstructed_time[i-1]
            i += 1
        
        return num_fleets