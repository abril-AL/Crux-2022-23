# **EEG Tinder Proposal**

-------------------------------------------------------------------------------------------------------------------------

## Narrative 

While the concept of “love at first sight” might seem like an over-romanticized myth, BCI technology can give insights into a more data driven perceived instantaneous attraction. Monitoring brain activity, we aspire to create a tinder like interface that swipes and selects matches based on a user's arousal. To achieve this, we will be studying mean frequencies/ activity responses when a participant is shown an image they find sexually exciting vs sexually boring.  

## Specific Aims

While several published attempts to measure facial attraction (specifically facial symmetry) have been conducted using eye tracking technology (Valuch et. al) (Kaiser and Nyga), limited published research features EEG as a way of measuring arousal responses to images. Besides a mate preference study examining feature vectors (observed lists) at alpha, beta, and theta frequencies and an unofficial BCI Youtube project that compared participants actual image preferences to predicted preferences, scientists have done little to explore EEG’s capability to detect sexual excitement (Yuan, et. al.) (The BCI Guys).  

Examining brain frequency changes upon visual arousal, we aim to deliver a tinder-like app controlled by an individual’s biodata. Researching an individual's reaction to images (unfamiliar faces that they rate as desirable or undesirable), we gain a deeper understanding of a person’s implicit preference in aesthetics. Technology that reveals such preferences can be valuable in neuromarketing fields and further applicable for creating accessible apps for paralysis patients. Thus, our products can lead to interdisciplinary innovation. Although future research would be necessary to broaden the applicable demographics, for this experiment, we are specifically testing subjects ages 18-22 at UCLA. 

  

 Within our 2 quarter timeline, our specific deliverables and goals are:

1.  Gain a deeper understanding into the changes in brain activity when aroused by an image. We will be monitoring alpha, beta, and theta brain waves in 8 spots spanning the frontal lobe, parietal lobe, and lateral occipital complex as a participant views an image. The higher the frequency derived from activity in the parietal lobe, the higher the perceived attraction. Waves in the beta range (14-30 Hz) will predictably be attributed for increased sexual arousal as they have in previous related studies (Guevara, et. al.). 
    
2.  Identify arousal on the spot with at least 75% accuracy. Comparing collected brain activity with a subject’s response to sexual desirability, over time, we hope to predict a person’s response without their explicit affirmation. Additionally, we hope that the app will filter out photos and track commonalities between “desirable” images so that over time it consistently shows images that the usr finds desirable. 
    
3.  Deliver an app that has learned to function based on spikes in brain activity with at least 75% accuracy. Using a calculated threshold found through our experiments, we hope to connect the data to an app that automatically swipes for a person. This app can further increase accuracy with machine learning as more experiments are done/ the app is used more often. 
    

Overall, our experiments and subsequent deliverables inquire: How does brainwave activity inform us about instantaneous attraction? Using Brain Controlled Interface (BCI) technology can we successfully record/predict “love at first sight” (or at least lust at first sight)? And finally, how can an application use brain data to automatically deliver the fruits of our research in a product? 

  

# Approach

  

## Strategy

This experiment is aimed to investigate the relationship between brainwave frequencies and arousal in the brain. The project will work to identify arousal in the brain and use physiological markers to confirm attraction on an app by swiping right, or deny attraction by swiping left. Over the course of the experiment the app will use arousal patterns to filter photos that fit the individuals “type”. 

## Potential Problems 

Potential challenges in our experimental design surround the images we select and the sexual preferences of those participating in the study. As the brain elicits a higher frequency upon seeing familiar faces and images with more eye-catching backgrounds, we will be using unfamiliar stock photos with blank backgrounds and similar lighting/filters (Verosky et. al). Even for deliberately high arousal image types (selected images which feature people in bikinis, shirtless, etc.), we will minimize background/ distracting elements. 

Another major problem with the transmission of EEG data to Open BCI is that there are often delays and chunks of data missing in the record. We aim to solve this issue through throwing out very skewed data (data missing huge chunks of information) and finding averages of frequencies within states. 

Additionally, in order to assure a person views an image as more sexually pleasing and not just aesthetically pleasing, we will only show images that reflect the participant’s sexual preference. Thus, separate image pools will be set and modified for straight female identifying women, straight men, and bisexual/pansexual participants. 

Finally, we aim to prevent aesthetic fatigue, desensitization after exposure to too many consecutive images, through testing and training our app in short bursts (Yang et. al). Subjects will be shown no more than 50 images at a time  (with a goal to show around 20-25 per individual) for 5 seconds at a time. If we notice that users commonly demonstrate lower arousal when viewing the last images in a set, we will lower the number of images shown per round. 

## Preliminary Studies 

Arousal in the brain is a hot topic of investigation and implementation. Previous studies have looked into the relationship between the P300 spike and arousal, and attempted to use this data into creating systems that anticipate an individual's interest in dating apps. Previous EEG studies regarding sexual desire in mentally deviant individuals also indicate that spikes in P300 are lower in neutral settings as opposed to both negative and positive-sexual ones (Steele). A decreased overall level of P300 may be something to watch out for, as previous studies have correlated it to risk factors such as aggression and frustration, which may be interpreted physically by the body as sexual arousal. 

Other studies have proposed that the P150-200 spike is more accurate for gauging arousal (Kaiser). There are multiple proposed ways of collecting and isolating the P300 spike. Some labs recommend the use of time-frequency decomposition technology in order to lower the alpha and lower beta bands. This method is useful in obtaining accurate (85.25%) results in asymmetry features (Yuan). Previous studies have also recommended implementing a normalization gaussian filter + a non-maximum suppression in the pre-processing stage. These additions have been proven to help improve identification ratio while reducing noise effects (Tsuda). Currently, there is no standard for what band-filter or frequency should be used during experimentation, but high success has been found when a 0.16–100-Hz band-pass filter and sampled at 512 Hz (Yuan). 

After data collection, previous studies have suggested utilizing General Linear Models (GLMs) to assess and analyze the EEG scans (Linden). Due to the high variety of brain scans necessary to evaluate all physical areas connected to sexual arousal, studies recommend using at least 9 GLMs. These areas are split into two categories, anteriority and laterality, with the former including categories of frontal, central, parietal, and the latter with left hemisphere, midline, and right hemisphere. Depending on how many given conditions we want to test, the number of GLMs can be calculated by the following formula: conditions x laterality x anteriority. 

# Experimental Design

Is it possible to measure the arousal of individuals? This experiment aims to prove that this can be accomplished by observing brainwave frequencies. We predict that arousal will be characterized by an increase in brainwave frequency (higher frequency: predictably in beta range (14-30 Hz) but this will be further calculated when analyzing data).   

*Phase I: Setting Up the App / Preparation*
-   We plan to use OpenBCI software and LSL to collect/process data which we will use to create a platform that can display photos and swipe either right (like) or left (dislike) based off of frequencies shown by EEGS (specifically checking to see if frequencies are in beta, alpha, or theta range) 
-   We will collect photos from stock images, public advertisement campaigns, free databases, etc. 
-   Commonalities between people in the images will be tracked/ manually entered by our experimenters: 
	1. Hair color
		- Black
		- Brown
		- Blonde
		- Red
		- Other  
	2. Race
		- Black 
		- White (non-hispanic) 
		- Hispanic (white)
		- Hispanic (non-white) 
		- Asian
		- Mixed Race/ ambiguous 
	3.  Piercings
		- Yes
		- No
	4. Tattoos
		- Yes
		- No
	5. Perceived Weight 
		- skinny/thin/fit
		- Midsize 
	6.  Eye color
		- Dark brown/black
		- Light brown/ hazel
		- Green
		- Blue/Gray
		- Other
	7. Age range
		- 18-25
		- 25-34
		- 35-45
		- 45-55
		- 55-65
		- 65-75+
	8. Makeup        
		- No makeup
		- Light-medium makeup
		- Heavy makeup

If time allows, we will further track quantitative facial metrics (measurements) as well. 

![](https://lh4.googleusercontent.com/Vnzf5UaQfPi4e3uKSud2oi4oZRpbtsDXEMdMqhnVi5FqOm0U2QYab0LekJ3kqJ0oJPexGzV9l2vSkyewa7Tc0icuZz33yId4kC8Gimynu5RUiXetm1O7Kf3b5ikwZe4YDJpcasV24Sgg7J-Ghy0reDE)

-   To find participants, we will advertise on social media, group chats, flyers on bruin walk, and bring in our friends 
    
*Phase II: Data Collection*
*Preliminary questionnaire:*
-   Individuals will be taken one at a time into controlled testing rooms that lack visual stimulation (We aim to have an equal number of male and female participants)
-   Individuals will be asked their gender identity and sexual preference (for the sake of this study we will only be examining heterosexual and bisexual/pansexual participants, not asexual participants.) 
-   The Pre-lab survey would look as forward: 
	1.  What gender do you identify as? 
		1.  Female     
		2.  Male
		3.  Gender queer/ gender nonconforming
		4.  Questioning
		5.  Prefer not to say 
	2.  What is your sexual preference? 
		1.  Heterosexual (female)
		2.  Heterosexual (male)
		3.  Homosexual (female)
		4.  Homosexual (male)
		5.  Bisexual/pansexual 
		6.  Asexual/other 
	3.  Is there any additional information we should know about your sexual preferences? 

*The experiment itself* 
-   An electrode headset will be connected to test subjects in 8 Spots: F3, F4, T3, T4, P3, P4 O3, and O4. 

![electrodes](https://user-images.githubusercontent.com/103137140/224883140-703ba57f-2809-443f-9fcb-f05df7931c5a.png)

-   Individuals will begin using the app and looking through the images (5 second per image followed by a 5 second break)  
-   While individuals are looking at images, voltages will be recorded every 4 ms
-   The frequencies of brain waves (data regarding the alpha, beta, and theta waves will be observed and recorded) through LSL
-   After each round, test subjects will record if they were attracted to the shown individual or not (see post-lab survey). 
    
*Post-experiment questions (order of questions rotated to counterbalance)* 
1.  Describe your “type” (only based on looks)? 
2.  Were there any images that specifically stuck out to you? 
3.  Did you recognize/ have you seen any of these images or faces before? 

Additionally: Images are shown again and participants and participants swipe again manually for the first couple of trials. 

*Phase III: Data Analysis*
-   Compare data between brainwave frequencies and recorded arousal states 
-   Find mean of an individual’s frequency between all images for comparison (this mean should increase through iterations) 
	-   Identify the most common trends in each category: hair color, race, piercings, tats, eye color, and perceived weight. 
	-   Compare facial measurements (optional) 
		-   Find the standard deviation between all images in a set 
		-   Identify the modes 
    
*Phase IV: App Training* 
-   App should show increased images of each preferred category (if the preference rate is over 50% [subject to change]) or look for the modes in each calculated facial measurement (most common spatial relationships +/- the standard deviation between facial measurements) 
-   Increments of more testing to reassess an individual's preferences 

Data Flow
![Diagrama de flujo](https://user-images.githubusercontent.com/103137140/224882789-38af74fc-a3b0-48d9-a8ad-e5ee94b36303.jpg)

## References

The BCI Guys. (2022). *I Swiped on Tinder with My Brainwaves! YouTube.* Retrieved February 11, 2023, from https://www.youtube.com/watch?v=pP7cASGL6bg. 

Bogaert, S., Masthoff, E., van Boxtel, G., & van der Linde, R (2022). EEG study on implicit beliefs regarding sexuality: Psychophysiological measures in relation to self-report measures. *Frontiers in Psychology*, 13. [https://www.frontiersin.org/articles/10.3389/ fpsyg.2022.930863/full](https://www.frontiersin.org/articles/10.3389/fpsyg.2022.930863/full). 

Guevara, M. A., Gómez-Navarro, C., Amezcua-Gutiérrez, C., Hernández-González, M., & Ågmo, A. (2018). Electroencephalographic correlates of sexual arousal induced by sexually-explicit reading in human females. *Journal of Behavioral and Brain Science*, 08(11), 599–614. https://doi.org/10.4236/jbbs.2018.811037 

Kaiser, D., & Nyga, K. (2020). Tracking cortical representations of facial attractiveness using time-resolved representational similarity analysis. *Scientific Reports*, 10(1). https://doi.org/10.1038/s41598-020-74009-9 

Valuch, C., PflÃ¼ger, L. S., Wallner, B., Laeng, B., & Ansorge, U. (2015). Using eye tracking to test for individual differences in attention to attractive faces. *Frontiers in Psychology*, 6. https://doi.org/10.3389/fpsyg.2015.00042 

Verosky, S. C., Zoner, K. A., Marble, C. W., Sammon, M. M., & Babarinsa, C. O. (2020). Familiarization increases face individuation measured with fast periodic visual stimulation. *Biological Psychology*, 153, 107883. https://doi.org/10.1016/j.biopsycho.2020.107883 

Yang, S., Zhao, Y., & Ma, Y. (2019). Analysis of the Reasons and Development of Short Video Application——Taking Tik Tok as an Example. 

Yuan, G., He, W., & Liu, G. (2022). Is mate preference recognizable based on electroencephalogram signals? machine learning applied to initial romantic attraction. *Frontiers in Neuroscience*, 16. https://doi.org/10.3389/fnins.2022.830820**



