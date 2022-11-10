<h4 align="center">Author: Karl Gardner<br>PhD Candidate, Department of Chemical Engineering, Texas Tech University</h4>

<div align="center">
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/154190573-53e361f6-7c60-4062-b56b-7cbd11d39fc4.jpg"/></a><br><br>
  
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/156635015-0cdcb0bb-0482-4693-b096-04f2a78f6b8e.svg" height="32"/></a>
  
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/201214903-9c9c1a02-8a04-494c-b784-14c24203f4aa.svg" height="32"/></a>

  <a href="https://www.depts.ttu.edu/che/">
  <img src="https://user-images.githubusercontent.com/91646805/156641068-be8f0336-89b5-43e9-aa64-39481ce37c94.svg" height="32"/></a>
  
  <a href="https://roboflow.com/">
  <img src="https://user-images.githubusercontent.com/91646805/156641388-c609a6aa-8fce-47f0-a111-abfde9c5da05.svg" height="32"/></a><br>
  
  <a href="https://www.sciencedirect.com/journal/chemical-engineering-journal">
  <img src="https://user-images.githubusercontent.com/91646805/201205256-eae01399-6813-46a1-ac6f-e3a33ad3d2fc.svg" height="32"/></a>

  <a href="https://colab.research.google.com/github/karl-gardner/nanofilm_data/blob/main/regression.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/201204243-a6179f59-575d-443c-8bf6-1384b1c835ab.svg" height="32"/></a>

  <a href="https://colab.research.google.com/github/karl-gardner/nanofilm_data/blob/main/chromaticity_bubble.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/201204458-be4da525-c57b-4fc5-9b15-5353dbd0515f.svg" height="32"/></a>



# Nanofilm Data
A colorimetric temperature-sensitive film has been reported for monitoring a wide range of temperatures with anticounterfeiting and sensor applications. The film has been prepared by layer-by-layer film deposition technique using chitosan solution (polycation) and carboxymethyl cellular azide (CMC-N3) solution (polyanion). We showed that the hydrophilic film could change the thickness by absorbing or desorbing moistures at different temperatures under fixed relative humidity (RH) and showed different uniform structural colors due to interference of light. The color-changing behavior in response to temperatures was tunable with respect to film thickness and RH. Furthermore, the film was patternable under UV light due to the azide group (-N3) in the polymeric backbone. The patterns stay hidden at room temperature which could be revealed in two ways under certain temperatures and RH: localized exposure to high relative humidity and spontaneous absorption of moisture under specific temperatures and RH. A simple correlation also reported for the prediction of thickness dependent behavior of the film with respect to temperature and relative humidity. Utilizing the pattern-revealing property and temperature sensitive color changing behavior, unique applications of the film as a temperature sensor was also demonstrated.
</div>

<img width="850" alt="image" src="https://user-images.githubusercontent.com/91646805/195671136-e5d19ef3-b5f3-46b9-a229-90c74b0341c2.png">


<details>
<summary>Instructions (click to expand)</summary>
<br>

1) First create a folder in your google drive account called nanofilm_data (This step is important in order to keep the directories in check)
2) Use this link <a href="https://drive.google.com/drive/folders/1KR24B7DwNcC6GkBWmuT2RmLLfYZm9Rxp?usp=sharing">
  <img src="https://user-images.githubusercontent.com/91646805/156700933-5cc77dba-5df1-40c0-94c8-7459abb6402b.svg" height="18"/></a> to access the shared google drive folder
3) At the top there will be a dropdown arrow after the folder location (Shared with me > data_files): click on this dropdown arrow
4) Click on the "Add shortcut to Drive" button then navigate to inside your nanofilm_data folder and click the blue "Add Shortcut" button.  This will add a shortcut to the shared google drive folder in your nanofilm_data folder.
5) Open the regression colab notebook from the colab badge provided, then click "Save a copy in Drive" under File > Save a copy in Drive.  Do the same for the provided chromaticity_bubble colab notebook.
6) This will save the two notebooks in the "Colab Notebooks" folder in your google drive.  Move these two notebooks to the nanofilm_data folder and rename them regression.ipynb and chromaticity_bubble.ipynb respectively in order for the directories to be correct.  The final nanofilm_data folder should look like this:<img width="720" alt="image" src="https://user-images.githubusercontent.com/91646805/201209147-3454e416-feac-42c3-a7ae-48592ea87b12.png">

</details>

<details>
<summary>Testing (click to expand)</summary><br>
Nearly all figures and tables from the paper are outlined in yolov3.ipynb and yolov5.ipynb colab notebooks. For example Table 2 displays the annotation summary for cell and droplet models before augmentations. This can be shown in section 2.1 of the colab notebook:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/186248580-b9d22a03-ee4f-451f-bd5e-19af2ee4fb01.PNG"/></a>
<br><br>
You may run this for example by first uncommenting section 1.1 labeled "Data with No Augmentation (No_Augmentation)":<br><br>
<img src="https://user-images.githubusercontent.com/91646805/186249216-0d38a78b-a25b-436e-919b-e94f19776039.PNG"/></a>
<br><br>
then uncommenting section 2. labeled: "For droplet model". Then the following output will be printed:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/186249418-e3420c46-20d0-4803-bd65-38fe8fb1bea1.PNG"/></a>
<br><br>
The same procedure can be used for the cell model to produce the following result:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/186249529-27c786d9-fb73-47a9-9590-dcc8f5fd277f.PNG"/></a>
<br><br>
This matches Table 2 in the publication:<br><br>
<img src="https://user-images.githubusercontent.com/91646805/186249617-8fddc568-d50a-443b-a4b3-fb9186071308.PNG"/></a>

</details>

<details open>
<summary>Contributions</summary><br>

 **Publication Authors:**<br>Md Nayeem Hasan Kashem, Karl Gardner1, Wei Li<br><br>
 
 **Publication Acknowledgements:**<br>W.L. thanks New Faculty Startup Funds from Texas Tech University (TTU) and funding support from Global Laboratory for Energy Asset Management and Manufacturing (GLEAMM) at TTU.
</details>
