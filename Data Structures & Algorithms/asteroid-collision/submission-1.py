class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids.pop(0)]

        for a in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and a < 0:
                prev_a = stack.pop(-1)
                collision_result = prev_a + a

                if collision_result == 0:
                    alive = False
                elif collision_result > 0:
                    alive = False
                    stack.append(prev_a)
                elif collision_result < 0:
                    alive = True
            
            if alive:
                stack.append(a)
        
        return stack


        # while asteroids:
        #     next_a = asteroids.pop(0)

        #     if (stack[-1] > 0) == (next_a > 0):
        #         stack.append(next_a)
        #     elif (stack[-1] < 0) and (next_a > 0):
        #         # will not collide
        #         stack.append(next_a)
        #     else:
        #         # (stack[-1] > 0) and (next_a < 0):
        #         prev_a = stack.pop(-1)
        #         collision_result = prev_a + next_a
        #         if collision_result != 0:
        #             if collision_result > 0:
        #                 stack.append(prev_a)
        #             else:
        #                 stack.append(next_a)
        
        # return stack



        #     # if (stack[-1] > 0) == (next_a > 0):
        #     #     stack.append(next_a)
        #     # else:  # different signs
        #     #     prev_a = stack.pop(-1)
        #     #     collision_result = prev_a + next_a
        #     #     if collision_result != 0:
        #     #         if collision_result > 0:
        #     #             stack.append()


