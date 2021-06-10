import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display


def getHapticaPattern(file,thr1=25,thr2=50,thr3=75,slot=0.1,plot=True):
    #Load audio data
    audio, sr = librosa.load(file)
    sample_duration = 1 / sr
    tot_samples = len(audio)
    duration = 1 / sr * tot_samples
    max=np.amax(audio)
    mean=np.sqrt(np.mean(audio**2))
    lim1=mean+(max-mean)*thr1/100
    lim2=mean+(max-mean)*thr2/100
    lim3=mean+(max-mean)*thr3/100

    #Preparing graph
    plt.figure(figsize=(8, 6))
    librosa.display.waveplot(audio, alpha=0.5)
    plt.ylim((-1, 1))
    plt.axhline(mean)
    plt.axhline(max)
    plt.axhline(lim1, color='g')
    plt.axhline(lim2, color='b')
    plt.axhline(lim3, color='r')

    plt.text(duration*1.02, (lim1+lim2)/2, '.', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 5})
    plt.text(duration * 1.02, (lim2 + lim3) / 2, 'o', style='italic',
             bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 5})
    plt.text(duration * 1.02, (lim3 + max) / 2, 'O', style='italic',
             bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 5})

    #Generating haptica pattern
    pattern=""
    for i in range(int(duration/slot)):
        lb=int(i*slot/sample_duration)
        ub=int((i+1)*slot/sample_duration)
        if lb>=0 and ub<=len(audio):
            currMax=np.amax(audio[lb:ub])
            currPattern='-'
            if currMax>=lim3:
                currPattern='O'
            elif currMax>=lim2:
                currPattern='o'
            elif currMax>=lim1:
                currPattern='.'
            pattern+=currPattern
    plt.title("Haptica Pattern : "+pattern)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude (Mapped between 0~1)")
    if plot:
        plt.show()
    return pattern

pattern=getHapticaPattern(file="ignition-start-3.mp3")
print(pattern)



