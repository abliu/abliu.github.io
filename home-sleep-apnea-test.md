# Home sleep apnea test

March 2024

tl;dr: For sleep apnea, I think I found a \~\$200 ownable at-home test
that measures most of what is measured in more expensive in-lab sleep
studies.

------------------------------------------------------------------------

Note: The information in this post is for general educational purposes
only and should not be construed as professional medical advice,
diagnosis, or treatment.

I was told by a sleep scientist that I should check every few years if I
snore, and if I snore, I should get tested for obstructive sleep apnea
(OSA). After recording myself with the iPhone app SnoreLab, I found that
I now do lightly snore some nights (0-5% of the time). The gold standard
test for sleep apnea is an overnight in-lab sleep study, but these can
have monthslong waits and cost thousands of dollars (even with
insurance![^1]). Your doctor can also prescribe you a cheaper, borrowed
take-home test provided by a sleep clinic, but such results can be
inaccurate and hard to verify due to equipment, clinic, or user
error.[^2]

People with sleep apnea have experimented with “DIY sleep tests” for at
least 18 years.[^3] After a week of research, my current best solution
is this [\~\$200 ownable at-home test
device](https://www.amazon.com/EMAY-SleepO2-Pro-Overnight-Continuously/dp/B09JSRT4R8/),[^4]
and it measures the critical metrics of nasal airflow and blood oxygen
saturation ([it works like
this](https://www.youtube.com/watch?v=awa4z2fFn7A) except without the
belt). These two metrics should be sufficient for detecting sleep apnea
and hypopnea events, [defined clinically as reductions in nasal airflow
and blood oxygen saturation which reflect reductions in
breathing](https://drive.google.com/file/d/1k9OdsZzi5xs3SP5vxWp1Z34Rak90bZGt/view).
The product may still have issues,[^5] but I’ll let a product review
describe the advantage of having such an at-home device:

> I’ve been using this product about 2x a week for the past month and
> I’ve been very impressed with the consistency and accuracy. My sleep
> doctor was as well, because this aligned perfectly with my lab
> results… \[Compared to owning this device,\] getting a snapshot \[with
> an at-home test *borrowed* from the sleep clinic\] was a pain… to pick
> up the device at a certain window across town, then drop it back off
> the next day… and what if the device slipped off, or disconnected?
> I’ve had that happen before, 3 weeks later when I finally meet with my
> doctor I’m told we have to do the test over again.”

Because you own the device, you can efficiently gather data from
multiple nights and test the efficacy of different sleep interventions
without lab reporting delays.[^6] You can also verify the data’s
accuracy with common sense[^7] and by recording sleep audio to see if
sounds of breathing align with airflow readings. I plan to get this if
my snoring continues.

Some caveats:

1.  *Nasal airflow and blood oxygen are not everything*: An in-lab sleep
    study additionally measures respiratory effort (with chest and
    abdomen belts) and arousals and sleep cycles with EEG. My
    understanding is that the belts are mainly needed to distinguish
    obstructive and central apnea events, but are not critical for
    detecting *whether* an apnea event has occurred. Consumer EEG
    headsets might be acquired separately; [here
    are](https://www.frontiersin.org/articles/10.3389/fninf.2020.553352)
    [two lists](https://learn.neurotechedu.com/headsets/) and the late
    [Zeo](https://en.wikipedia.org/wiki/Zeo,_Inc.) was an EEG headband
    specifically designed for sleep. Sleep cycles might be measured by
    other wearables based on accelerometer, heart rate, temperature, and
    other biometrics.[^8]
2.  *Not all at-home devices are equal*: Given the relatively cheap and
    comprehensive device above, I would not trust an at-home device that
    did not measure both nasal (and/or oral) airflow *and* blood oxygen.
    Unfortunately, it seems that many at-home sleep test devices are
    only [watches](https://www.youtube.com/watch?v=PVyvWqhKArg), rings,
    or iPhone apps; they do not measure airflow via nasal cannula. The
    WatchPAT ONE in particular is [widely
    prescribed](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883090/)
    and [marketed as an accurate at-home
    test](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7052958/) but is
    actually only [61% accurate in classifying
    normal/mild/moderate/severe
    OSA](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883090/), likely
    because it does not measure nasal airflow.[^9]
3.  *There may be better at-home sleep test solutions out there.*
    [SleepData](https://www.sleepdata.com/) and [the SLP SleepStrip (now
    ApneaStrip)](https://sleepsense.com/shop/apneastrip/) may be better;
    I haven’t researched them yet.

## Footnotes

[^1]: I talked to three friends who got sleep studies done. Two paid
    thousands of dollars with insurance while one got it essentially for
    free.

[^2]: I have a friend who got a take-home test from a clinic which
    incorrectly said he was healthy when he actually had severe sleep
    apnea. He thinks the misdiagnosis might have been due to
    aforementioned reasons of faulty equipment, user error in attaching
    the equipment, and/or clerical error of mixing up patient reports.
    Other general reasons for inaccuracy: [the test might not measure
    key metrics like
    airflow](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8883090/), the
    equipment might get disconnected during the tossing and turning of
    sleep, or the clinic might not provide detailed data which can be
    checked against common sense and a sleep audio recording.

[^3]: [This 2006 wiki article on
    cpaptalk.com](https://www.cpaptalk.com/wiki/index.php/Sleep_Study_Tests)
    mentions [SleepData](https://www.sleepdata.com/), an active
    take-home sleep test provider, as well as [the SLP SleepStrip (now
    ApneaStrip)](https://sleepsense.com/shop/apneastrip/) and the
    seemingly discontinued Accutest SleepStrip. [This 2009 post on
    cpaptalk.com](https://www.cpaptalk.com/viewtopic/t38597/Doityourself-sleep-study-components.html)
    details an at-home sleep lab with the following components: a
    Respironics M Series APAP with card reader, software, and pressure
    gauge (to both assist and measure breathing); a CMS-50F recording
    pulse oximeter; a Sony Camcorder with night vision; and a
    SleepTracker Pro sleep watch. Although the providers of at-home
    tests have shifted, it seems that nasal airflow, blood oxygen, and
    respiratory effort (plus EEG in in-lab studies) have remained the
    core components of sleep tests for all this time.

[^4]: Amazingly, this EMAY SleepO2 is 1 of only 2 nasal
    airflow-measuring at-home sleep apnea tests I could find on Amazon.
    The other Amazon product is from [Snore
    Circle](https://www.amazon.com/dp/B0C2TR5JTS) but lacks the oximeter
    and has fewer reviews. ResMed sells the [ApneaLink
    Air](https://www.resmed.com/en-us/healthcare-professional/products-and-support/home-sleep-testing/apnealink-air/)
    but I think they sell mainly to healthcare providers and not
    directly to consumers.

[^5]: Amazon reviews mention unresponsive support and data export
    problems.

[^6]: A possible exception: You *might* not be able to test CPAP if the
    CPAP mask blocks the at-home device’s nasal cannula for measuring
    airflow. However, you can still use the finger oximeter and the CPAP
    might have your breathing data.

[^7]: For example, if you know you woke up in the middle of the night
    and took off the nasal cannula, and the device is showing that as an
    apnea event, you can discount that.

[^8]: The [Oura
    ring](https://www.sciencedirect.com/science/article/pii/S1389945724000200)
    takes this approach.

[^9]: Perhaps there will be more research into improving the WatchPAT
    ONE’s accuracy by gathering more paired watch oximeter and nasal
    airflow data and improving machine learning models that can infer
    the latter based on the former; until then, I’d rather trust devices
    that measure nasal airflow.
