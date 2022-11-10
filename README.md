<h4 align="center">Author: Karl Gardner<br>PhD Candidate, Department of Chemical Engineering, Texas Tech University</h4>

<div align="center">
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/154190573-53e361f6-7c60-4062-b56b-7cbd11d39fc4.jpg"/></a><br><br>
  
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/156635015-0cdcb0bb-0482-4693-b096-04f2a78f6b8e.svg" height="32"/></a>
  
  <a href="https://www.depts.ttu.edu/che/research/li-lab/">
  <img src="https://user-images.githubusercontent.com/91646805/201203491-77f0f264-f11f-4381-95e0-516ec25574f4.svg" height="32"/></a>

  <a href="https://www.depts.ttu.edu/che/">
  <img src="https://user-images.githubusercontent.com/91646805/156641068-be8f0336-89b5-43e9-aa64-39481ce37c94.svg" height="32"/></a>
  
  <a href="https://roboflow.com/">
  <img src="https://user-images.githubusercontent.com/91646805/156641388-c609a6aa-8fce-47f0-a111-abfde9c5da05.svg" height="32"/></a><br>
  
  <a href="https://www.sciencedirect.com/journal/chemical-engineering-journal">
  <img src="https://user-images.githubusercontent.com/91646805/201202867-415be87e-dfd7-4c95-a215-b9a0ef96446d.svg" height="32"/></a>
  
  <a href="https://colab.research.google.com/github/karl-gardner/droplet_detection/blob/master/yolov3.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/201204243-a6179f59-575d-443c-8bf6-1384b1c835ab.svg" height="32"/></a>

  <a href="https://colab.research.google.com/github/karl-gardner/droplet_detection/blob/master/yolov5.ipynb">
  <img src="https://user-images.githubusercontent.com/91646805/201204458-be4da525-c57b-4fc5-9b15-5353dbd0515f.svg" height="32"/></a>

  <a href="https://github.com/ultralytics">
  <img src="https://user-images.githubusercontent.com/91646805/156641066-fbc3635b-f373-4cb7-b141-9bcaad21beff.svg" height="32"/></a>



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
5) Open the 3d_data colab notebook from the colab badge provided, then click "Save a copy in Drive" under File > Save a copy in Drive.  Do the same for the provided yolov5 colab notebook.
6) This will save the two notebooks in the "Colab Notebooks" folder in your google drive.  Move these two notebooks to the droplet_classification folder and rename them yolov3.ipynb and yolov5.ipynb respectively in order for the directories to be correct.  The final droplet_classification folder should look like this:<img width="720" alt="image" src="https://user-images.githubusercontent.com/91646805/148874654-890a5d94-f9e9-4273-bcd8-318df44feca4.png">

7) Find the droplet model dataset here: <a href="https://universe.roboflow.com/karl-gardner-kmk9u/pc3dropletdetection2/dataset/8">
  <img src="https://user-images.githubusercontent.com/91646805/156698861-29c0ae55-eff3-4bfe-9dcc-fe06e5a1c6cd.svg" height="18"/></a> and you will see two datasets (No_Augmentation and final_dataset).  Start with the final_dataset and click on "Download" in the upper right corner.  Then, click "Sign in with Github" and follow the prompts to allow roboflow to sign in with github.  Or you may create a different account with roboflow.  Then, the download link will bring you to a pop up that says Export.  For the "Format" click on the YOLO v5 PyTorch and "show download code" on the bottom.  You will then see a link that you can use to enter in the colab notebook.  The final page should look like this but with your own link under the red stripe: <img width="925" alt="image" src="https://user-images.githubusercontent.com/91646805/149068681-5d5529b4-7d6f-41f5-8710-98f04c780654.png"> Then copy this link into the section of both notebooks (yolov3.ipynb and yolov5.ipynb) that says "Curl droplet data from roboflow > Data with Augmentation for Training > [ROBOFLOW-API-KEY]": ![image](https://user-images.githubusercontent.com/91646805/151044698-1d03e6c8-7d2b-401c-b632-b00d1fbe6821.png)  Copy your download link inside of the double quaotations as in the red box in the image provided.

8) Repeat step 7 for the droplet dataset with no augmentations (No_Augmentation): ![image](https://user-images.githubusercontent.com/91646805/151045660-a4fb9e26-a108-4369-aba9-63be2bb9efc1.png)

9) Repeat steps 7 and 8 with the cell dataset <a href="https://universe.roboflow.com/karl-gardner-kmk9u/cropped_drops2/dataset/3">
  <img src="https://user-images.githubusercontent.com/91646805/156698862-6591ba12-a90f-4495-8736-cab83f5cd237.svg" height="18"/></a>
10) You can now use both notebooks to perform more testing or contribute to the project.  You can find the code written for many of the figures in the final paper: DOI Website
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
