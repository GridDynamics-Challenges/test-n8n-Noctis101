## The Scenario
You are building the data processing pipeline for a fleet of high-altitude survey drones. The drones return altitude data as arrays of integers, but the sensors occasionally glitch, recording negative numbers that must be ignored. 

### The Challenge (3 Levels)
This is a **progressive** coding challenge. You are expected to build upon and refactor your code as you advance through the levels. **Do not copy-paste monoliths; reuse your functions.**

* **Level 1 (Target: 15 mins):** Write two functions: `cleanData(arr)` to filter out any negative altitude readings, and `findPeak(arr)` to find the highest altitude in the cleaned array.
* **Level 2 (Target: 30 mins):** Build upon Level 1. Write `calculateElevationGain(arr)`. This function must take raw drone data, clean it, and calculate the total upward climb (sum of all positive altitude changes between consecutive points).
* **Level 3 (Target: 45 mins):** The system now receives an array of arrays (multiple drone flight paths). Write `findSteepestPath(matrix)`. Identify and return the specific flight path that has the highest continuous elevation gain. *Your solution must be highly optimized for Time and Space complexity.*

---

### How to Write and Test Your Code
For this assessment, you will be using a fully integrated cloud environment called **GitHub Codespaces**.

**How to Start:**
1. On your repository homepage, click the green **<> Code** button.
2. Click the **Codespaces** tab.
3. Click **Create codespace on main**. 
4. The environment will take about 1-2 minutes to build. Once it loads, you will have a full VS Code editor with a live terminal at the bottom of your screen.

**Your Testing Loop:**
1. **Code:** Write your logic in your preferred language folder (`/Python`, `/Java`, or `/JS_TS`).
2. **Test:** Use the integrated terminal at the bottom of the screen to run your tests locally (e.g., `pytest`, `npm test`, or `mvn test`). You do not need to commit your code to see if it works!
3. **Commit & Push:** Once your tests pass, click the "Source Control" icon on the left sidebar to commit and push your work.

---

### Final Submission
When you have completed all three levels (or when the 1.5-hour timer is up):
1. Ensure all your final code is committed and pushed.
2. Create a new branch called `submission`.
3. Open a **Pull Request** from your `submission` branch into `main`. 
4. **Do not merge the Pull Request yourself.** Leave it open. Our AI Review Agent will automatically grade your PR for modularity and complexity.
