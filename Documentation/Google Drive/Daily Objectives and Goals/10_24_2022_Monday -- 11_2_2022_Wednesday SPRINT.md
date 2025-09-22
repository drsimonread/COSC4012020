**CDSpec Project Sprint Objectives 10/24 – 11/2/2022**

Resources

* [QA CDSpec Availability File](https://docs.google.com/spreadsheets/d/14XzB-l-NpYjzZifEgkJxYghMT_p-vZwYvjKJIBBWDvk/edit#gid=1513700858): Fill out any days you think you won’t be in class (clubs, sports, birthday, etc.)  
* [SRS Document](https://docs.google.com/document/d/18O2LRt3E-uxt3SPEOAuJy9GEFfvscALflvwEWL9Wu6o/edit)  
* [.py Comment Completion Records](https://docs.google.com/document/d/1zTsihsIW3v96RbcZC0JXa9UiWBMPcBhcXQ92a19tgI4/edit)  
* [.py Files Relationships Model](https://lucid.app/publicSegments/view/540c904a-497b-4721-8d67-7b1291875402) (Link may need fixing)

QA

- [ ] Everyone should have Docker installed on their system  
- [ ] Finish Tracing .py files to [SRS](https://docs.google.com/document/d/18O2LRt3E-uxt3SPEOAuJy9GEFfvscALflvwEWL9Wu6o/edit) requirements  
      - [x] ~~Make new Traceability Matrix: will trace .py files to requirements~~  
      - [ ] Refer to [this document](https://docs.google.com/document/d/1zTsihsIW3v96RbcZC0JXa9UiWBMPcBhcXQ92a19tgI4/edit) for the new Traceability Matrix; R\&D will be starting to fill this out  
- [ ] Make list of .py files which R\&D needs to debug/fix based on failed requirements

R\&D

- [ ] Finalize .py Files Relationship Model/ Diagram  
      - [ ] When finished, I want both teams to discuss the structure so that everyone can understand how the program functions  
- [ ] Address any comment concerns QA has  
      - [ ] Add to comments that QA doesn’t understand fully  
- [ ] Download Docker  
      - [ ] [How to Instructions](https://docs.google.com/document/d/1IMU35kl0ulgNxhSOdS2LPHouUOrKbKyj/edit)  
      - [ ] [Visual Instructions to help](https://docs.google.com/presentation/d/10_vgcaxQ5PLeU1MqoB549S5asWC75yHS/edit#slide=id.p1) (Slides 3-15; Sysops and I get error after slide 15, if you don’t let us know)  
      - [ ] If you run the Docker Image of our program, you may have to run **wsl \--shutdown**  in your command prompt or reset your PC after running the Docker, since it likes to still use VMMEM/RAM after closing down the app.

SysOps

- [ ] Traceback Docker errors  
      - [ ] Build a local certificate so that Docker can be run locally as well as globally  
- [ ] Demonstrate to QA and R\&D how to set up a local certificate so everyone can have access to a local deployment  
      