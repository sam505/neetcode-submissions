class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        track = []

        for i, temp in enumerate(temperatures):
            if not track:
                track.append(i)
                continue

            if temp > temperatures[track[-1]]:
                results[track[-1]] = i - track[-1]
                track.pop()
                
                while track and temp > temperatures[track[-1]]:
                    results[track[-1]] = i - track[-1]
                    track.pop(-1)
                
                track.append(i)
            else:
                track.append(i)
        
        return results

