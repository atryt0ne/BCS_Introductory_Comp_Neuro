
SUMMARY
# VIDEO 1: INTRO TO BRAIN SCIENCE
20% of oxygen used by brain
Functional localization-
for example;
*In the neocortex:*
Primary visual cortex, primary auditory cortex, primary motor cortex, broca’s and Wernicke’s area,etc.
*In the subcortical regions(evolutionary older)*
Hypothalamus, amygdala, etc.

## HARDWARE OF THE BRAIN: 
### 1)	NEURONS
Neurons communicate through action potentials-currency of information processing
we have around 86 billion neurons in human brain
### 2)	SYNAPSES
Connections between two neurons-electrical or chemical type
in chemical type-the pre synaptic axon releases neurotransmitters into the post synaptic dendrite that bind to their receptors—giving rise to deflection in the membrane potential
Deflection can be of two types- excitatory(+ve) or inhibitory(-ve)—dale’s dogma
## BRAIN’S CONNECTIVITY-NEOCORTEX
1 cortical sheet-->2M macrocolumns-->200M minicolumns-->20B neurons
Info input into layer 4---goes to layer2/3—goes to layer 5/6—to higher and local cortex
Brains large scale connectivity: neocortex
86B neurons—10T synapses—100k miles of axon length—220mphaxon conduction speed
Brain is therefore a network of networks


# VIDEO 2: PSYCHOPHYSICS

## definition

it is the the analysis of perceptual processes by studying the effect on a subject's experience or behaviour of systematically varying the properties of a stimulus along one or more physical dimensions
can be described to be a relation between stimulus and sensation
example-trichromacy(rgb)--humam color perception

## why study it
The precise measurement of perception enables one to form theories about the underlying neural representation.
example-weber fechner law--smallest noticeable change
for weight perception the JND was 5%--
heavier the original weight, larger is the external change required to percieve the difference

## how to do psychophysics
### detection task
What is the minimum detectable amount of light?
in order for us to see it is necessary for only 1 quantum of light to be absorbed by each of 5 to 14 retinal rods
you conduct light detection experiments with volunteers and record the probablity of them detecting the light at a certain amount and draw a graph
#### The detection threshold is a special case of JND –the “just noticeable difference” from zero. How to measure the threshold?
*  *Method of constant stimuli*
●Take many measurements at several fixed stimulus values. Fit a curve and deduce the threshold.
●Pro: Highly reliable.
●Con: Very time-consuming
* *Staircase procedure*-more efficient
Try and figure out roughly where the threshold is and focus trials on that, homing in as you go. 
●Pro: Much faster than Method of Constant Stimuli.
●Con: A few early errors can throw it off –better to average several staircase measurements.
●More complex to code but several libraries exist

#### point of subjective equivalence-perception biases

Key goal of neuroscience to relate all human experience (!) to neural activity.
●Start by relating sensory perception to neural activity.
●This necessitates the precise measurement of perception.
●Rigorous techniques developed to measure sensitivity, perceptual biases while avoiding confounds due e.g. to decision criterion or response bias.


# VIDEO 3: BEHAVIORAL READOUTS
## why readout behavior
as scientists we need to relate behaviour to neural activity

Example behavioral readouts of
-Decision making
-Complex movements
-Learning/memory
-Internal state
## to study decision making
a common way is to use a two alternative forced choice task
for example- a delayed 2afc task with mice
1)Handles come in
2)Mouse grabs handles -> initiates trial
3)Stimuli at random time after (2x)
4)1 second delay
5)Animal licks one spout to indicate decision
another example-Body part tracking with DeepLabCut

### two types of movements by subject animals
1) task related  -Timing of handle grabs-Timing of licks-Choice-Success
2) uninstructed  -Hindlimb movements-Pupil diameter-Whisking-Low dimensional representation
**Cortex-wide activity dominated by movement, especially uninstructed movement!**

*Behavioral readout of learning/memory:Morris Water Maze*
before learning- random trial paths
after learning- straight path towards the target

*measuring internal state-for example fear*
Indirect measure: mice freeze when they are scared

*using eye-tracking to record attention*

# VIDEO 4: LIVE IN LAB
Anne Churchland's lab at UCLA studies the neural circuits behind decision making
Softwares such as DeepLabCut(to record body movements) and Wide field imaging(to record neural activity) are used to collect data.

## wide field imaging setup
consists of 2 different modules--an excitation module where there's a blue LED which sends light straight to the mouse's cortex, which excites the GCaMP that sends the green light back which is sent into the camera that records and acquires data. After hemodynamic correction and making a skull preparation, we can generate the image of the entire dorsal skull of the mouse.


# VIDEO 5: BRAIN SIGNALS- SPIKING ACTIVITY

## properties of neurons
basic units of nervous system--communciation using electrical signals that travel along the following path
dendrites-->cellbody/soma-->axon-->synapses

## action potentials
- they are rapid changes in polarity of the membrane potentials caused due to differences in concentration of Na+ and K+ ions inside and outside(more positively charged) of the cell membrane that creates a gradient/potential difference(-70 mV).
- there exist channels within the membrane that allow selective ions to pass through. Influx of Na+ ions(makes inside more positive) and efflux of K+ ions(makes the inside negative again) causes rapid flips in polarities.

## electrophysiology--recording spikes
- spikes represent action potentials fired by individual neuron which are very small in nature so they need to be amplified.
- spike patterns are fundamental to coding in brain--all vital info is coded within spike pattern and frequency
- action potential threshold must be reached for spike to be recorded
- each neuron has maximum firing frequency(refraction period)
- there are voltage gated channels within the membrane which sometimes can be leaky
- all electrical properties of neurons are subject to change.

## connections
interconnected neurons give birth to an array of networks properties
there can be
- forward excitation
- feedforward inhibition
- feedback inhibition
- feedback excitation
neurons that have endogenous bursting activity can help set up rhythmic behaviours. central pattern generators have been identified in various networks.











