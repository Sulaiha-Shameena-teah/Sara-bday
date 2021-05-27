from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, UserComments, BdayComment
import sys
import django
from django.conf import settings
from django.conf.urls.static import static


Birthday_wishes = [
    ['Sakthi abirami', 'Happy Birthday Sara!!!😍 Eppaum pola jolly ah iru da❤️😇Vera enna solla therila da...🥺 Anbu jastiya agiduchuna ippadi dhan vai adichu poiduvaen😅 😘 nalla iru da poda... Wish you all success da🔥🔥🔥'],
    ['Prathisha', 'Happy Birthday Sara 😍 Naama spend pana days la romba memorable athu inum extend aga porathu ninaicha naa romba excited ha irukaNee un health parthuko 😇Yaar ena sonalum un mind la potukatha nee un life la ena pananum nu ninaikriyo atha panu All the best for ur future❤️ Miss you and Live you lots❤️'],
    ['Sakthi Siva Parvathi', 'Saraaa exam hall partner uh..many more happy returns of the day da...god bless you...nalla ponnu nalla frnd enaku...en mokka jokes thaangitu ena uyire oda vitadhuku nanri da 😂...love u chlm..will stay in touch..happy birthday ❤️'],
    ['Shravani',
        'Happy birthday ra Sara bhai(topper girly) 🧐future Walmart ceo😻🤣🤣🤣ceo ana enga ellarkum anga oru Vela vangi kudu  🤣🤣🤣🤣FINAL TOUCH =SENGIL CHUKHA HAMNIDA  🤣❤️SARANGHAEYO'],
    ['Sumuja', 'Happy Birthday sara🎂🎉 my cute topper and sweet pondatti 😘😍 I wish that this year would be great and successful year for you.. love you so much chellakutti ❤️'],
    ['Madhangi', 'Happy birthday sara❤️❤️ Happy ah iru life la and stay the same.'],
    ['Supraja',
        'Happy bday Sara chellame ❤️❤️ I still remember those days when you used to rag me cutely ( Na evlo periya rowdy nu therinjum 😂🙀 ). Ena vasigara pada soli kalachadhu and more 😂😂. College mudiya podhu hope our bond doesn\'t 🥺❤️Wishing you all luck and success for future endeavours don 😂😍'],
    ['Abirami', 'happy birthday oorkari♥️ be happy dont worry🤷🏻‍♀️ we have loads of memory😘 nee iladha bus trip misery🎎 nee dhan d en company💣 [PS: read it in tr voice]-with love abi♥️'],
    ['Santhosh', 'En pulla sara...nee ena avlo fair ah... lockdown la adikuthu sema bore ah... Happy b\'day exam theivamey...wish u all success and healthy life...🎂🕺'],
    ['Thejeshwar', 'Hey Sara, thankyou for always supporting, motivating and being my side.. Apdilam sola mudyathu, apdi sona over ah panuva.. I just wanted to tell you that don\'t be the same, evolve and get more better.. Ippadiku Batman..'],
    ['Sona', 'Heyy sara .....hello dear💓 happy happy born day ma...still i remember our frst meeting in my room of 105 with all our frnds🥰🤗......keep smiling ..tension aagama life la pudichaa unaku thevapaduradha pannu....yeppovum happy ah iruu☺️🥳....njoy the fullest of life💓🥰all good breezy things will reach at right time❄️❄️stay happy stay blessed💟'],
    ['Indrani', 'Many more happy returns of the day Sara. You are most amazing talented lovable person ever. Hope you will be very happy and joyful all the time and all your wishes come true'],
    ['B Aparna', 'Happieee bdy sara!😍 May this day and all your days  be filled with love, joy, laughter, and happiness. Once again many many happy returns of the day roomieee🧁🎂🤩'],
    ['Kavya', 'Many more happy returns of the day Sara.Nee romba nalla ponnu lam solla maten😂. Ellar kudaiyum easy ah pazhagiduva, enkudaiyum apadi dhan frnd ana, yeduva irundalum straight forward ah solliduva, olivu maraivu illama. Unkita pesunah time porardhe theriyadhu, but nee romba neram la pesavum maate 😂. Unkita pidichadhe sincerity dhan, enda work irundha sikiram mudichidanum nu nenaipa. Enkuda nee adigama pesunadu illa, irundalum nee epaiyum oru nalla caring friend. Happy Birthday once again.'],
    ['Swathi', 'Happiest birthday sara😍💜.. Enjoy your life... Always be happy..stay safe and stay healthy..keep smiling🥰'],
    ['Dr. Nithya', 'Happy birthday Saraaaaaaaa 💗..best friend n Fav person ever ..tq for being with me even in the hardest part in my life 😝'],
    ['G M Sahithi', 'Many more happy returns of the day sara. Wish you a lot of success and happiness. Keep smiling😊'],
    ['Raheema', 'Hii Sara Chlakutty😍😘❤️..Wish U a happpyyyyy Birthday dear🥳🤩....So blessed to have a trustworthy❤️ friend like U😚...Glad to have U..enaku mattum ila..enga vtla ellarukum una first lenthe rmba pudikum🤩..avlo spl nee engluku🥰..want this bond for lifetime...💝...Life la perusa achieve pananum🎯🥇😇...Love towards U never end❤️'],
    ['Kaviya', 'Happieeeeee b\'day sara✨🥳 wish u to reach gr8 heights🔥stay happy  and with the same charm ever da💓'],
    ['Nithya', 'Hi Sara..wish you a very happy birthday😍🎊Be happy and keep smiling as always♥️'],
    ['Swetha', 'Happy b\'day sara❤️,Epovum happy ah iru d..un kooda iruntha time la romba spcl athu la epovum marakathu.Namma evalo kevalama sanda potalum Namma kulla iruka bonding epovum pogathu..Athu long lasting...🥰.Ithae mathiri Namma frndship epovum continue aaganum nu aasa padran..Etho inaiku un bday ah atha una pathi ena la nallatha solla mudiyum nu romba yosichu yosichu kashta pattu solirkan..bcoz una pathi nallatha solla en kita ethuvum ila🤣..Epdiyo po nalla irunthu thola..En asirvatham epovum unaku irukum.'],
    ['Shameena', 'Happy Birthday Sara(sars)❤️😊...you are my sister fairy☃️ just without wings😂...we have been together for 1366 days..🔥..day 1 la nee eppdi irunthiyo...apdiye Iruka..🥰.. having a beautiful supportive kind hearted frnd is a blessing...and I got that😂😅'],

]


def index(request):
    '''
    for i in UserComments.objects.all():
        i.delete()
    '''
    pics = Image.objects.all()
    pics = list(pics)
    img_clr = ['b017e7f', 'bc11a2b', 'b68ff00',
               'b052939', 'bFFBF00', 'bff005c']
    length = len(pics)
    a = []
    while len(a) < length:
        a += img_clr
    a = a[:length]
    ziplist = zip(pics, a)
    return render(request, 'index.html', {'ziplist': ziplist})


def puzzle(request):
    bcomments = Birthday_wishes
    person, wishes = [], []
    for i in Birthday_wishes:
        person.append(i[0])
        wishes.append(i[-1])
    img_clr = ['red', 'orange', 'violet', 'purple', '#006FFF',
               '#13f4ef', '#68ff00', '#faff00', '#FFBF00', '#ff005c']
    length = len(bcomments)
    a = []
    while len(a) < length:
        a += img_clr
    a = a[:length]
    ziplist = zip(person, wishes, a)
    return render(request, 'puzzle.html', {'bcomments': bcomments, 'ziplist': ziplist})


def comment(request):
    if request.method == 'POST':
        username = request.POST['username']
        comment = request.POST['comment']
        ins = UserComments(username=username, comment=comment)
        ins.save()
        print(username, comment)
        usercomments = UserComments.objects.all()
        img_clr = ['red', 'orange', 'violet', 'purple', '#006FFF',
                   '#13f4ef', '#68ff00', '#faff00', '#FFBF00', '#ff005c']
        length = len(usercomments)
        a = []
        while len(a) < length:
            a += img_clr
        a = a[:length]
        ziplist = zip(usercomments, a)
        return render(request, 'comment.html', {'ziplist': ziplist})
    usercomments = UserComments.objects.all()
    img_clr = ['red', 'orange', 'violet', 'purple', '#006FFF',
               '#13f4ef', '#68ff00', '#faff00', '#FFBF00', '#ff005c']
    length = len(usercomments)
    a = []
    while len(a) < length:
        a += img_clr
    a = a[:length]
    ziplist = zip(usercomments, a)
    return render(request, 'comment.html', {'ziplist': ziplist})
