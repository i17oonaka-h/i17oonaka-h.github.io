---
layout: page
title: "Wave-Trainer-Fit: Neural Vocoder with Trainable Prior and Fixed-Point Iteration towards High-Quality Speech Generation from SSL features"
description: Submitted to ICASSP 2026
img: assets/projects/thumbnails/wave-trainer-fit.png
importance: 1
category: research topic
related_publications: false
---
---
<font color="#646536">
Authors: <b>Hien Ohnaka</b>, Yuma Shirahata, Masaya Kawamura
</font>
[[~~arxiv~~]()][~~code (will be available)~~]
<br>

### Table of contents
- [Background and Motivation](#background-and-Motivation)
- [Proposed method](#proposed-method)
- [Overall results](#overall-results)
- [Speech samples](#speech-samples)
    - [Compared to baselines](#compared-to-baselines)
    - [Impact of intermediate outputs](#impact-of-intermediate-outputs)
    - [SSL layer-wise analysis](#ssl-layer-wise-analysis)
- [References](#references)
<br><br>

### Background and Motivation
With the development of recent self-supervised learning (SSL) models, generation tasks from SSL features have also achieved success [1, 2]. 
Neural vocoders from SSL features are crucial components that determine the topline in these tasks.
WaveFit [3] is a vocoder that has already achieved success in speech generation tasks from SSL features [1, 2]. 
This is a fixed-point iteration vocoder that combines GANs with diffusion model-like iterative inference.

However, compared to the waveform generation from Mel-spectrogram, WaveFit from SSL features has two limitations:

1. Initial noise sampling
    - WaveFit from mel-spectrograms: Well-designed noise sampling [4] is available. <font color="#00369f">This approach is expected to provide the model with an reasonable prior for waveform generation</font>, but <u>this is required spectral envelope information.</u>
    - <b>WaveFit from SSL features: Because the spectral envelope cannot be accessed from SSL features, Sampling from a standard normal distribution $\mathcal{N}(0,I)$ was used. <font color="#b71c1c">Compared to the approach mentioned above, this may compromise performance.</font> </b>
2. Gain adjustment
    - WaveFit from mel-spectrograms: Following gain adjustment for predicted waveform $z$ is performed using the power $P_z$ of the output and <u>the ground-truth power $P_c$ from the mel-spectrogram</u>: $\mathcal{G}({z}_t,{c})=\sqrt{(P_c/(P_z+s)}{z}_t.$ <font color="#00369f">As a result, the vocoder is freed from the implicit energy estimation task and can focus on essential waveform modeling.</font>
    - <b>WaveFit from SSL features: Because ground-truth power cannot be accessed from SSL features, the following reference-free gain adjustment was applied: $\hat{\mathcal{G}}({z}_t)=0.9 \cdot {z}_t/\max(\mathrm{abs}({z}_t)).$ <font color="#b71c1c">This adjustment compromises the advantages mentioned above.</font></b>

<b>Our goal is to improve the performance of WaveFit from SSL features by bridging these gaps when compared to WaveFit from mel-spectrogram. 
To achieve this, we introduce trainable priors inspired by RestoreGrad [5].</b>
<br>

### Proposed method
<div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/projects/thumbnails/wave-trainer-fit.png" title="example image" class="img-fluid rounded z-depth-1" %}
        Figure 1: Overview of the proposed model. During training, Posterior VAE derived from the target waveform and the SSL feature is used for noise sampling and gain adjustment. During inference, Prior VAE derived from the SSL feature is used for same process. Solid arrows are enabled during both training and inference.
</div>

We propose a neural vocoder with <b><u>train</u></b>abl<b><u>e</u></b> prio<b><u>r</u></b> and <b><u>f</u></b>ixed-point <b><u>it</u></b>eration (<b><u>WaveTrainerFit</u></b>) for improved waveform generation from SSL features. <font color="#00369f"><b>First, by introducing variational autoencoder (VAE)-based trainable priors, we achieve sampling of noise $\mathcal{S}(\Sigma)$ close to target waveform. Since inference can start from a point close to speech, high-quality waveform generation with fewer iterations and robustly maintaining speaker characteristics is expected. Furthermore, by imposing constraints on the priors to match the energy of speech, we realize reference-aware gain adjustment $\mathcal{G}_\mathrm{ssl}(z_t, \Sigma)$, which frees the vocoder from the implicit energy inference task. As a result, the model can focus on more important aspects of waveform modeling, and is thought to mitigate the difficulty of training.</b></font>
<br>

### Overall results
We used the LibriTTS-R corpus [6]. For evaluation, we used the speech included in “test-clean”.
We used three feature extractors for conditioning features: WavLM [7], XLS-R [8], and Whisper-medium-encoder [9].

<div class="col-sm mt-3 mt-md-0">
Table 1: Evaluation results when using LibriTTS-R test-clean, 8-th layer SSL features, and $T=5$. <b>Bold</b> indicates the best method under the same conditions, and <u>underlines</u> indicate significant differences between WaveFit and WaveTrainerFit.
{% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/overall_results.png" title="example image" class="img-fluid rounded z-depth-1" %}
</div>
<br>

### Speech samples
<br>

##### Compared to baselines

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>260_123288_000023_000005</u><br>(middle-pitch, male)
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Transcription.<br>"My eyes fail under the dazzling light, my ears are stunned with the incessant crash of thunder."
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_wavlm8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_wavlm8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_wavlm8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_xlsr8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_xlsr8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_xlsr8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_whisper8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_whisper8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000023_000005_whisper8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>8555_284449_000041_000001</u><br>(high-pitch, female)
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Transcription.<br>"I'll have 'Sizzle make a fine yard for the goat, where he'll have plenty of blue grass to eat."
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_wavlm8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_wavlm8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_wavlm8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_xlsr8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_xlsr8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_xlsr8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_whisper8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_whisper8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/8555_284449_000041_000001_whisper8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>1188_133604_000024_000000</u><br>(low-pitch, male)
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Transcription.<br>"But in this vignette, copied from Turner, you have the two principles brought out perfectly."
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_wavlm8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_wavlm8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_wavlm8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_xlsr8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_xlsr8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_xlsr8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_whisper8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_whisper8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1188_133604_000024_000000_whisper8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>1995_1836_000030_000000</u><br>(middle-pitch, female)
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Transcription.<br>"But you mean to say you can't even advise her?"
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_wavlm8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_wavlm8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_wavlm8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_xlsr8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_xlsr8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (XLS-R)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_xlsr8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        HiFi-GAN (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_whisper8_hifigan-v1.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_whisper8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (Whisper)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/1995_1836_000030_000000_whisper8_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<br>

##### Impact of intermediate outputs

<b>Objective evaluation results</b>
{% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/metrics_intermediate_outputs.png" title="example image" class="img-fluid rounded z-depth-1" %}
<font color="#00369f"><b>Although the introduction of VAE slightly increases the RTF, the proposed method shows superior scores in all metrics except for the RTF, at all iteration counts.</b></font>

<b>Speech samples</b>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>4507_16021_000032_000001</u><br>"Is it really the French tongue, the great human tongue?"
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (Whisper, l8)
        Iteration 0 (Normalized initial noise)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavefit-0.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavefit-0.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (Whisper, l8)
        Iteration 0
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavetrainerfit-0.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavetrainerfit-0.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 1
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavefit-1.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavefit-1.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 1
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavetrainerfit-1.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavetrainerfit-1.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 2
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavefit-2.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavefit-2.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 2
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavetrainerfit-2.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavetrainerfit-2.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 3
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavefit-3.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavefit-3.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 3
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavetrainerfit-3.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavetrainerfit-3.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 4
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavefit-4.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavefit-4.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 4
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavetrainerfit-4.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavetrainerfit-4.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 5
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavefit-5.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavefit-5.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 5
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/4507_16021_000032_000001_whisper8_wavetrainerfit-5.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/4507_16021_000032_000001_whisper8_wavetrainerfit-5.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>5105_28241_000027_000002</u>: "Nothing was to be done but to put about, and return in disappointment towards the north."
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (Whisper, l8)
        Iteration 0 (Normalized initial noise)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavefit-0.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavefit-0.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (Whisper, l8)
        Iteration 0
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavetrainerfit-0.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavetrainerfit-0.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 1
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavefit-1.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavefit-1.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 1
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavetrainerfit-1.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavetrainerfit-1.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 2
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavefit-2.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavefit-2.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 2
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavetrainerfit-2.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavetrainerfit-2.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 3
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavefit-3.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavefit-3.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 3
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavetrainerfit-3.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavetrainerfit-3.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 4
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavefit-4.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavefit-4.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 4
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavetrainerfit-4.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavetrainerfit-4.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit Iteration 5
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavefit-5.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavefit-5.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit Iteration 5
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/5105_28241_000027_000002_whisper8_wavetrainerfit-5.mp3" controls=true %}
        {% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/5105_28241_000027_000002_whisper8_wavetrainerfit-5.png" title="example image" class="img-fluid rounded z-depth-1" %} 
    </div>
</div>

##### SSL layer-wise analysis
Generally, features from shallow layers are known to contain many acoustic features from the input samples, while features from deeper layers contain many semantic features from targets such as pseudo-labels. 
To verify whether the proposed method works robustly for features of various properties, we evaluated it on WavLM layers 2 and 24.

<b>Objective evaluation results</b>
{% include figure.liquid loading="eager" path="assets/projects/contents/wave_trainer_fit/imgs/table_layer_wise_ablation.png" title="example image" class="img-fluid rounded z-depth-1" %}

<b>Speech samples</b>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>121_127105_000008_000000</u>: "I quite agree--in regard to Griffin's ghost, or whatever it was--that its appearing first to the little boy, at so tender an age, adds a particular touch."
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM, l2)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_wavlm2_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM, l8)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_wavlm8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM, l24)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_wavlm24_wavefit-5.mp3" controls=true %}       
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM, l2)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_wavlm2_wavetrainerfit-5.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM, l8)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_wavlm8_wavetrainerfit-5.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM, l24)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/121_127105_000008_000000_wavlm24_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<br>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <u>260_123288_000004_000001</u>: "The atmosphere is charged with vapours, pervaded with the electricity generated by the evaporation of saline waters."
    </div>
    <div class="col-sm mt-3 mt-md-0">
        clean
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_clean.mp3" controls=true %}
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM, l2)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_wavlm2_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM, l8)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_wavlm8_wavefit-5.mp3" controls=true %}       
    </div>
    <div class="col-sm mt-3 mt-md-0">
        WaveFit (WavLM, l24)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_wavlm24_wavefit-5.mp3" controls=true %}       
    </div>
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM, l2)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_wavlm2_wavetrainerfit-5.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM, l8)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_wavlm8_wavetrainerfit-5.mp3" controls=true %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        Proposed WaveTrainerFit (WavLM, l24)
        {% include audio.liquid path="assets/projects/contents/wave_trainer_fit/260_123288_000004_000001_wavlm24_wavetrainerfit-5.mp3" controls=true %}
    </div>
</div>
<font color="#00369f"><b>It can be heard that our proposed method works robustly in terms of naturalness even from features that lack acoustic information.</b></font>
<br>

---
### References
[1] Y. Koizumi, H. Zen, S. Karita et al., “Miipher: A robust speech restoration model integrating self-supervised speech and text representations,” in Proc. of IEEE WASPAA, 2023, pp. 1–5.<br>
[2] T. Saeki, G. Wang, N. Morioka et al., “Extending multilingual speech synthesis to 100+ languages without transcribed data,” in Proc. of IEEE ICASSP, 2024, pp.11,546–11,550.<br>
[3] Y. Koizumi, K. Yatabe, H. Zen et al., “WaveFit: an iterative and non-autoregressive neural vocoder based on fixed-point iteration,” in Proc. of IEEE SLT, 2022, pp.884–891.<br>
[4] Y. Koizumi, H. Zen, K. Yatabe et al., “SpecGrad: Diffusion probabilistic model based neural vocoder with adaptive noise spectral shaping,” in Proc. of Interspeech, 2022, pp. 803–807.<br>
[5] C. H. Lee, C. Yang, J. Cho et al., “RestoreGrad: Signal restoration using conditional denoising diffusion models with jointly learned prior,” in Proc. of ICML, 2025.<br>
[6] Y. Koizumi, H. Zen, S. Karita et al., “Libritts-r: A restored multi-speaker text-to-speech corpus,” in Proc. of Interspeech, 2023, pp. 5496–5500.<br>
[7] S. Chen, C. Wang, Z. Chen et al., “WavLM: Largescale self-supervised pre-training for full stack speech processing,” IEEE J. Sel. Top. Signal Process., vol. 16, no. 6, pp. 1505–1518, 2022.<br>
[8] A. Babu, C. Wang, A. Tjandra et al., “XLS-R: selfsupervised cross-lingual speech representation learning at scale,” in Proc. of Interspeech, 2022, pp. 2278–2282.<br>
[9] A. Radford, J. W. Kim, T. Xu et al., “Robust speech recognition via large-scale weak supervision,” in Proc. of ICML, vol. 202, 2023, pp. 28,492–28,518.
