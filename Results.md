## Methods: 

 - We chose 5 open source projects to see how likely are the participants to contribute to these and asked them to compare this with the Constable score.
 - We monitored the debugging session with each participant to understand their thought process and kept track of the time they spent on each repository. 
 - We also questioned them on how like are they to use this application in the future and what are the additonal features that they would like to see. 

## Materials: 
1. Git repositories: 
  - AWS Acc Shread - https://github.com/openshift/aws-account-shredder
  - Scikit learn - https://github.com/scikit-learn/scikit-learn
  - Dark Error Holes - https://github.com/MrL1605/Dark-Error-Holes
  - Expertiza - https://github.com/expertiza/expertiza
  - Starship - https://github.com/starship/starship
2. Apllication link - https://whispering-cove-85016.herokuapp.com/
3. Survey Link - https://forms.gle/7e2RejWu4uWdw8MV8
4. Monitored zoom session 

## Observations:
<img width="606" alt="Screen Shot 2020-11-16 at 7 23 52 PM" src="https://user-images.githubusercontent.com/69658606/99324147-9ef87380-2841-11eb-8240-141080fc05b8.png">

The afore-mentioned chart describes the scores that were awarded to each repository. For each repository, we have collected the mean score awarded by each participant to that repository, mode (maximum count) of the score awarded by each participant to that repository and the score awarded by the Github Constable Application to that repository. We observed that the participants looked for code coverage, issues description, badges in README files as some of the important measures before awarding the scores to the repositories. Whereas on the other hand, the Github Constable Action project analyzed the repositories for the presence of certain files like License, Contributing, etc. for awarding the score to the repositories.

<img width="607" alt="Screen Shot 2020-11-16 at 7 25 21 PM" src="https://user-images.githubusercontent.com/69658606/99324164-a7e94500-2841-11eb-8865-29837fb0952c.png">

The responses from the lab participants w.r.t the question "is the Constable app was useful and would you use it?" gave very different results as shown above. As the stats show 48% of the participants absolutely found the app useful and interesting, while 12% gave it a 4/5 rating and 29% rated it 3/5. A small percentage of 9.7% showed a disinterest in using the app and did not find it useful therefore rating it low value. The reason some of the participants did not find it useful were is because it lacked a few features which they were looking for in the app.

<img width="607" alt="Screen Shot 2020-11-16 at 7 25 31 PM" src="https://user-images.githubusercontent.com/69658606/99324166-a9b30880-2841-11eb-8302-97bee56a1f58.png">

The chart above shows the score awarded by the participants regarding how easy is the application to install and sue. Most of the participants believed that the app was easy to install since all they had to do was open a URL and login with their github credentials. However 1-2 participants believed that since they had to own the repositories for which they want to get the score for and they had to sign in with their git accounts it was not as easy. Overall, we got good responses for this one.

![seproj3](https://user-images.githubusercontent.com/69658606/99326247-f00a6680-2845-11eb-9ff6-6304496c3516.jpeg)
=======

This chart shows the amount of time taken by each participant for calculating the score for the git repos manually and using constable. We can see that 6 / 10 participants took less time while using constable than while calculating it manually. This could mean that constable is helping people save time. However, due to the small size of responses this is inconclusive. 


## Suggesstions by Lab Participants:

-  "The app would be better if it checks inside individual files to and then rate them. "

-  "Include issues (closed and open), commits (are descriptive), number of contributors and documentation as a factor too."

-  "Considering the content and usability of README.md and code coverage "

-  "Weighted Scoring of each metric considered"
-  "I'd like to see it tracking the code coverage and if code build passes or not. Also, currently I can use the application on my repositories only. I'd like to see Constable working on other public repositories as well. "


## Conclusion:

We derive the following conclusion from the lab trials: 

- Constable does a good job in identifying some major files ( such as LICENSE.md ) in a repository. Although it does not scrutinize those files like a human would do.
- 77.4% of participant gave the rating of 4+ out of 5 in the lab trials, which means they found it really useful and were willing to use it.  
- 70% of the participant found constable easy to install .
- Constable is helping users save time. 60% people took less time with constable. However, due to the small size of responses this is inconclusive. 

## Threats to validity: 

- **Repeated Testing:** Some of the participants have also picked the same project to test. This causes a conflict of interest in terms of materials used for evaluation and the kind of responses we received. 
- **Public repository and easy availability of every groups code:** We believe that since all the repositories links are freely available to all the other students, it could have been a possibility that some of the subjects have referred to the implementations before their trial giving them an unfair advantage over the other subjects. This would have impacted the results of our trial unknowingly.
- **Sample Population Difference:** We picked 5 git repositories for the trial. It is a possible threat that there could be other repositories out there which are either harder to diagnose or easier to diaognose by both participants and the application itself. If this is the case, our results may not be as accurate. 
- **History of subjects:** Subjects come from different backgrounds, for example, some may be more familiar with android development and some more familiar with cloud data services. It is a possibility that when posed with a repository that is not familiar to them they might produce flaky results. It could also be the case that if they are too experienced in the field, they might produce very specifiv results. This would cause an inconsistency in the expectation of what factors the score should include. 
