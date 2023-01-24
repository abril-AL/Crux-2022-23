 # Team 12 - Abril , Lit Review
 - The first two sources look at yes/no situations related to Signal processing/EEG signals
 - They are similar to the idea we have to "swiping left or right"
 
 
 ## Source #1 - Research of brain activation regions of "yes" and "no" responses by auditory stimulations in human EEG
 [Link to article](spiedigitallibrary.org/conference-proceedings-of-spie/8201/82011K/Research-of-brain-activation-regions-of-yes-and-no-responses/10.1117/12.905015.full?SSO=1)
 ### Abstract
 <details><summary>Most EEG-based BCI systems make use of...</summary> well-studied patterns of brain activity. However, those systems involve tasks that indirectly map to simple binary commands such as "yes" or "no" or require many weeks of biofeedback training. We hypothesized that signal processing and machine learning methods can be used to discriminate EEG in a direct "yes"/"no" BCI from a single session. Blind source separation (BSS) and spectral transformations of the EEG produced a 180-dimensional feature space. We used a modified genetic algorithm (GA) wrapped around a support vector machine (SVM) classifier to search the space of feature subsets. The GA-based search found feature subsets that outperform full feature sets and random feature subsets. Also, BSS transformations of the EEG outperformed the original time series, particularly in conjunction with a subset search of both spaces. The results suggest that BSS and feature selection can be used to improve the performance of even a "direct," single-session BCI.
 </details>
 
 ### Main Takeaway
- This research mentions that some methods of studying patters "require many weeks of biofeedback training" So it might be of use to look into their mehods of shortening this. Most importantly, they mention a "single session." 
- They do mention the importance of <kbd>yes</kbd>/<kbd>no</kbd> inputs, similar to what we want to achieve with <kbd>right</kbd>/<kbd>left</kbd> swiping
- The pdf version is available on the link, but will also be available on my [google drive](https://drive.google.com/drive/folders/1YluR8_p_E4_v1FoM2XDLxqdWgAUc1U_1?usp=sharing)

### Within the paper
- Definitions
    - There are a few more terms mentions of importance to the research: BSS, GA, and SVM
    - Blind Source Separation (BSS) - BSS refers to a problem where both the sources and the mixing methodology are unknown, only mixture signals are available for further separation process. [IEEE](https://ieeexplore.ieee.org/document/6709849)
    - Genetic Algorithm (GA) 
    - Support Vector Machine (SVM) 
 - Methods
    - Experiment Procedures  
        - The subjects were shown one of the words “yes” or “no” on a computer screen
        - Participants were told to hold the image of what they chose in their heads
        - The yes/nos were equal but in random order,
        - First two trials , one yes and one no, were ignored for experimental setup
    - EEG Recording 
        - 32 electrode EEG device, except electrodes FC4 and FCZ
            - out of our reach..
        - **Important** : The study focused on the bipolar VEOG and HEOG electrodes commonly used to monitor blinks and eye movement artifacts. All other electrodes were referenced to physically linked mastoids
        - Software: They used the Matlab implementation of Infomax available as part of the EEGLAB software


## Source #2 - Feature Selection and Blind Source Separation in an EEG-Based Brain-Computer Interface
[Link to article](https://link.springer.com/article/10.1155/ASP.2005.3128)

### Abstract
<details><summary>People with neuromuscular disorders are difficult to communicate with the outside world...</summary> It is very important to the clinician and the patient's family that how to distinguish vegetative state (VS) and minimally conscious state (MCS) for a disorders of consciousness (DOC) patient. If a patient is diagnosed with VS, this means that the hope of recovery is greatly reduced, thus leading to the family to abandon the treatment. Brain-computer interface (BCI) is aiming to help those people by analyzing patients' electroencephalogram (EEG). This paper focus on analyzing the corresponding activated regions of the brain when a subject responses "yes" or "no" to an auditory stimuli question. When the brain concentrates, the phase of the related area will become orderly from desultorily. So in this paper we analyzed EEG from the angle of phase. Seven healthy subjects volunteered to participate in the experiment. A total of 84 groups of repeatability stimulation test were done. Firstly, the frequency is fragmented by using wavelet method. Secondly, the phase of EEG is extracted by Hilbert. At last, we obtained approximate entropy and information entropy of each frequency band of EEG. The results show that brain areas are activated of the central area when people say "yes", and the areas are activated of the central area and temporal when people say "no". This conclusion is corresponding to magnetic resonance imaging technology. This study provides the theory basis and the algorithm design basis for designing BCI equipment for people with neuromuscular disorders.
</details>

### Main Takeaway
- The abstract mentions: "This paper focus on analyzing the corresponding activated regions of the brain when a subject responses "yes" or "no" to an auditory stimuli question." which is somewhat similar to how we want to look at patterns in out EEG date
- However, note that it explicity mentions auditory stimuli, while our study is more to do with visual stimuli
- The full pdf of the paper can also be found on my [google drive](https://drive.google.com/drive/folders/1YluR8_p_E4_v1FoM2XDLxqdWgAUc1U_1?usp=sharing)

