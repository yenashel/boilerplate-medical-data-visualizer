# Medical Data Visualizer

This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer

# Attribution
KM, 10.06.2024: I had quite a hard time to get the tests working and it turned out at the end that my Seaborn v0.12.2 was causing the issues. In particular I did not get the numbers in the heatmap squares working (they only appeared in the upper row when I remember correctly). An update to v0.13 finally solved the issue. 

In the meanwhile I was using fuzzyray's solution as a reference for debugging (https://github.com/fuzzyray/medical-data-visualizer.git)

My final resulting code does not look that much different from this. I assume that the exercisess predefinend structure and the explanations provided basically ensure that everybody's code at the end looks pretty much the same.

In contrast to fuzzyray I was using lambdas for flagging the "ones" in #3 and I was using a different aggregation strategy for the categorical groupby.

My heatmap looks pretty much the same as I likend my code very much to his in the course of debugging Seaborn's v0.12.2 flaws