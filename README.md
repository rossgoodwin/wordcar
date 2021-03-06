# WORD CAR

![Word Car Cadillac XTS](http://i.imgur.com/dgG3hXP.jpg "Word Car | Photo by Christiana Caro")
*Photo by Christiana Caro*

This repository contains the raw code from [Ross Goodwin](http://rossgoodwin.com)'s Word Car experiment of March 2017, in which he (accompanied by: Lily Beale-Wirsing, Beth Goodwin, Christiana Caro, Kenric McDowell, Nora Hamada, Lewis Rapkin, & David Smoler) drove a 2017 Cadillac XTS from Brooklyn, NY, to New Orleans, LA.

![Axis M3007 pan-tilt-zoom surveillance camera](http://i.imgur.com/2hmUG9C.jpg "Axis M3007 | Photo by Christiana Caro")
*Photo by Christiana Caro*

Goodwin outfitted the car with an Axis M3007 pan-tilt-zoom surveillance camera on the trunk that could look in four directions at once; a GPS unit connected to an onboard database of [Foursquare](https://foursquare.com) locations; and his Razer Blade laptop, which used its microphone to record conversation inside the car and its clock to record the time at every moment. These elements, combined with [long short-term memory recurrent neural networks](https://en.wikipedia.org/wiki/Long_short-term_memory) that Goodwin trained to write poetry and prose, created an automatic narration of the entire journey. (Neural network implemention included [Torch-RNN](https://github.com/jcjohnson/torch-rnn) and [Densecap](https://github.com/jcjohnson/densecap) by [Justin Johnson](https://github.com/jcjohnson/), which must be present to run any code in this repository.)

The complete narrative was printed onto thermal paper in real time using a Datamax O'Neil MF4T wide format thermal printer, resulting in 11 scrolls:

![11 scrolls of Word Car](https://i.imgur.com/LpNF8Ul.jpg "11 scrolls of Word Car")

To read Kenric McDowell's (of Google's [Artists and Machine Intelligence](http://ami.withgoogle.com) program) account of the trip, with photos by Christiana Caro, see [his essay on Medium](https://medium.com/artists-and-machine-intelligence/ai-poetry-hits-the-road-eb685dfc1544).

The code in this repository is intended to be an open source contribution, licensed under GPLv3. Certain elements critical to running the Word Car software in its intended state, including the neural network models Goodwin trained, will be added in the future. The complete narration the machine produced will also be published, and linked to this page at some point in the future.

## Leaving Bushwick

    2017-03-25 09:17:34
    It was nine seventeen in the morning, and the house was heavy.

    2017-03-25 09:53:46
    It was seven minutes to ten o'clock in the morning, and it was the only good thing that had happened.

    2017-03-25 09:54:23
    What is it? the painter asked.

    2017-03-25 09:54:43
    The time was six minutes until ten o'clock in the morning, and the wind stood as the windows were freshly covered with boxes.

    2017-03-25 09:57:17
    The time was three minutes to ten o'clock in the morning, and the conversation was finished while the same interview was over.

    2017-03-25 09:57:35
    It was three minutes to ten o'clock in the morning, and the sheets of coal had been broken.

    2017-03-25 10:36:11
    7777777777777>>>>>>>>>>>>>>>>>>>>>>>>>>>>>77777>77777777777777777777777777777777777777777777777777777777777777777777777777777777
    77777777777777>>>>>>>>>>7>>77>>>>>>>>>>>>>>>>7777777777777777777777777777777777777777777777777777777777777777777?7?????????777??
    777777777777777777777>7777777777>>>7>>>>>>>>>777777777777777777777777777777777777777777777777777???7?77?777777??????????????????
    777777777777777777777777777777777777>>>>7>>>7777777777777777777777777777777777777777777777?7????????????????????????????????????
    77777777777777777777777777777777777777777>>>7>777777777777777777777777777777777777777777????????????????????????????????????????
    7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777????????????????????????????????????????
    777777777777777777777777777777777777777777777777777777?7?777777777777777777777777777????????????????????????????????????????????
    777777777777777777777777777777777777777777777777777777??77777777777777777777??????77?????????????????????????C???????????????CCC
    7777777?7??????777777777777777777777777777777????????????777777777777777777????7?????????????????????????????C??CCCCCCC?C??????C
    7777?777?7?????77??????7???????????7777?7????????7??????????7777777777777??????????????????????????C?CCCC???CC?CCCCCCCCCCCCCCCCC
    ???????????????????????????????????777777???????????????????????77???????????????????????????????C?????CC????C???CCCCCCCCCCCCCCC
    ?????????????????????????????777????7?7?????????????????????????????????????????????????????C?????????????????????CCCCCCCCCCCC?C
    ???????????????????????????????????????????????????????????????????????????????????????C??C?CC??C???CC?????????????CCCCCCCC???CC
    ??????????????????????????????????????????????????????????????????????????????????????CCCCCC?CCC?CC?CCC?CCCCCCCCCCCCCCCCCCCCCCCC
    ?????????????????????????C???C?CCC?CCC?C?????C?CCCCCCC?C??????????C????????????????CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    ????????????CC?CC?C???CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCCC??????????????????????CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC???CCC
    CCCCCCCCCCCCCCCCCCC?CCCCCCCC?CCCCCCCCCCCCCCCCCCCCCCCCCCC?CCCC?C????????CC???CCCCCCCCCCCCCCCCCCCCCCCCCCCCC????CCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCCCCCCCC????????????CCCCCCCCCCCCCCCC?
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCC??CC??????C???CC??CCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCCCCC?CCCCCCC????CCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCOCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?????CCC???CCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC???CCCCCCC????CCCC????CCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?C?CCCCCCCCCCCCCCCCCCC
    OCCCCCCCCCCCCCCCCCCCCCCCOOCCCCCOCCCCCCCCOCCOOOOOOOCCCOCCCCCCCCOOCCCCCCCCCCCCCCCCCCCCCCCCCCOCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCOCCCOOCCCCCCCCCCOCCCOOCCOCOCOOOCOCOOCOOOOOOOOOOOOOOOOOOOOOOOCOOCOOOOOOOOOCCOCCCCCCCCCOOOCCCCCCCCCCCCCCCCCCCCCCCCCCOOOOCCCOCOCC
    $OOCCCCOCCC?COCCCCOCOCCCOCCCOCCQCCCCOCOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO$OOOOOOOOOCOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    O$O$$OOOOOOQCO$$$$$$$$OOOOOOOOO$$$$$$O$OOOOOOOOOOOOOOOOCOOOOOOOOOOOOOCOOOOCCCOCCC$OOOOOOOOCCCOOOOOOOOOOOCCCCCCCCCCCCCCCCCOCCCCOC
    QQQ$$$$$$OOH$$$$Q$Q$$Q$$$$$OOOO$$QQQQQQQO$$$$$OOOOOOCOCOOOOOO$$OO$OOOOCOOOOOOOCOOOOOOOOOOO$O$OOO$OOOOOCCCCCCCCCCCCCCCCOCCCCCCCCC
    HHHHHHQQQQHQQQQ$OOQQ$$QQQQ$QQOOQH$$O7OQHQQQQQQ$OOO$$$$$O$$Q$Q$$$$$$$$$$$$O$$$OOOQCOOOOCCOCOOOOOOCOOOOOOOCCCCCOOOCCOOOOOOOOOOOOCC
    HQQQQHQQQQQQQQHHQ$$$$$$$O$Q$OOO$$$$QQQQQQHQQQQQQQQQQQQQQQQQQQQQQQHQQQQQQQQ$O$$QQQ$$OOOOO$$OOO$OOO$CO$OOOOOOOCCCOCOOCOOCCOCCOCOOC
    HHHHQHHHHHHHHHHQHQHHQHHHHQHQQQQQQQQQQQ$QQ$O$$QQQQQQQQQQQQQQQQQQQQQQHHHQQQQQQQQQQQQQQ$$$$$QQQQQ$Q$QQQHQQOOOOOOCOOOCOOOO$$O$$OOO$O
    HHHHQHHQHHHQHHHHHHHHHHHHHHHHHHHHQHHHQHHHHHHHHHHHHHQHHQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ$$QQQQQQQQQQQQQQ$QQ$QQ$$$$$$$$O$$$QQQQQQQ
    HHHHHHHHHHHHHHHHHHHHHHHHQHHHHHHHHHHHHHHHHHHHHHHHHHQHHHHQQHHHHQHQQQQQQQQHHHHHHHHHHHHQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQO$QQHQQQHQQHH
    A patch of green grass seemed to be seeking its face, but it was not much to see. A small patch of grass had already been stretched along the sidewalk, and the steps of the barn were locked.

    2017-03-25 10:42:52
    It was ten forty-two in the morning, and the driver had to stay alone and start back from the parking lot.

    2017-03-25 10:43:15
    It was ten forty-three in the morning and the crowd was set in a small street. The windows were still alive. The grandfather was hanging on the main road.

    2017-03-25 10:47:04
    It was ten forty-seven in the morning, and the door opened and the bar stood up and a dark sky came closer.

    2017-03-25 10:47:25
    The time was ten forty-seven in the morning, and the picnic showed a past that already had hair from the side of the track somewhere in the middle of the room.

    2017-03-25 11:21:21
    What are you doing here? he asked.

    2017-03-25 11:25:48
    CCCCC?CCC??C???????????????????????????????????????????????????????????????????????????????CC???????CC?C??????C??C????C?????????
    CCC????C????????????????????????????????????????????????????????????????????????????????C?C?????CC???????C??CC?C??????C????C????
    ?????????????????????????????????????????????????????????????????????C????????????C????CC?CCCCC???C?CCCCCCCCCCCCCCC?C?C???????C?
    C?CCC???????????????????????????????????????????????????C?C?????????????????????CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC??????????
    C??CC?????????????????????????????????????????????????C???CC???????????CC???C??C??CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC???C???C
    CCCCCCC?C?????????????????????????????????????????????????C???????CCC?CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?C?CCCC
    CCCCCCC?CCC?CCCCCCCC?????????????????????????????????????C??C??????CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCC??C?C???C????????????C?????????C?CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCC?CCC?C?????CCCC?CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC?
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC$QC?CCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCOOQCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCOCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCOCCCCCCCCCCC
    OOCOOCCCOCCCCCCCCCCCCCOCCCOCCCOCCOCCOOCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCOCCCCC?CCCCCCCCCCC
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCOOOCCCCC$CCCCCCCCCCCCCCCCCCCCCCCCOCOCCCOCOCC
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCOOOOCCQCCCCCCOCCCCCCCCCCCCCOOOCHO$$Q$$$$$
    OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOCOOOCCOCCCCCCCCCCOCCCMMMMMMCCCCOCCCCCCCCCCCCCCCCCCCCCOO$OOOOCCCCCCCC$CCOOOOCOOOQ$$$$OOOO$QQHHHH
    OOOOOOOOOOOOOOOOOOOOOOOOOCCCCCCCCCCCCCCCOMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM$OOCOOOCOOOOOOO$$OOOOOOOCOQHQQQQQQQQQQQQQQ$$QQ$Q$OQQQQ
    OOOOOOOCOOOOOOOCCCCCCCCCCCOCOOOOCOCMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM$$$$$$OO$OCO$OOO$$QHHHHHHHHHHQ$$$$$OQQQHQHHHQ$QQ
    OOOCOCOOOOOOOOOOOOOOOOOOOOO$QQQMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMQQQQQQQQQQQ???????CC??7QHQQHHHHHHHHQQ$$QQQ$Q
    OOOOOOOO$O$OO$$OO$$QQ$QQQQQHMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMQQQQQQQQHHQHHHQ$$$$Q$$QQQQQQQQQQQQQQQQQQ
    $$$$$QQQQQQQQHQQHHHHHHHHMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMHHHHHHHHHHHHHHHHHHHHHHHHHHHHQHHQQHQHH
    HHHHHHHHHHHHHHHHHHNHNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNHHNNNNHNHHHHHHHHHHHHHHHHHHHHHH
    NNNNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    NNNNNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNMNNNNNNNNNNNNNNNNNNNNNNNNNN
    NNNNNNNNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNMNNNNMNNNMMNNNNNNNNNN
    NNNNNMNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNMMNMMNMNMMNNNMMMNNN
    NNNNNNMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNMMNNNNNNNMNMMMMMNM
    NNNNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNMMNNMNMNMNNMNN
    NNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNMNNN
    NNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNNN
    NNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNNN
    NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNNN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNNN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNNN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNNN
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNNNNNNN
    The sky is blue, the bathroom door and the beam of the car ride high up in the sun. Even the water shows the sun.


## License

    Word Car automotive narration system
    Copyright (C) 2017, Ross Goodwin

    Full license at: https://github.com/rossgoodwin/wordcar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    You may contact Ross Goodwin at ross.goodwin@gmail.com or send physical correspondence to:

        Ross Goodwin c/o ITP
        721 Broadway, 4th Floor
        New York, NY 10003
