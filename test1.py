from flask import Flask, request, render_template, redirect, url_for
import random
import sys
import os
import math

test = []
list1 = []
app = Flask(__name__)
counter = 0
compare = 0
intercept = -7.248873208
calculatedvalue = 0




array2 = []
for i in range(0,224):
    array2.append(0)

dictionary= {'Anti-Mage':1,
'Axe':2,
'Bane':3,
'Bloodseeker':4,
'Crystal Maiden':5,
'Drow Ranger':6,
'Earthshaker':7,
'Juggernaut':8,
'Mirana':9,
'Morphling':10,
'Shadow Fiend':11,
'Phantom Lancer':12,
'Puck':13,
'Pudge':14,
'Razor':15,
'Sand King':16,
'Storm Spirit':17,
'Sven':18,
'Tiny':19,
'Vengeful Spirit':20,
'Windranger':21,
'Zeus':22,
'Kunkka':23,
#'Arc Warden':24,
'Lina':25,
'Lion':26,
'Shadow Shaman':27,
'Slardar':28,
'Tidehunter':29,
'Witch Doctor':30,
'Lich':31,
'Riki':32,
'Enigma':33,
'Tinker':34,
'Sniper':35,
'Necrophos':36,
'Warlock':37,
'Beastmaster':38,
'Queen of Pain':39,
'Venomancer':40,
'Faceless Void':41,
'Wraith King':42,
'Death Prophet':43,
'Phantom Assassin':44,
'Pugna':45,
'Templar Assassin':46,
'Viper':47,
'Luna':48,
'Dragon Knight':49,
'Dazzle':50,
'Clockwerk':51,
'Leshrac':52,
'Natures Prophet':53,
'Lifestealer':54,
'Dark Seer':55,
'Clinkz':56,
'Omniknight':57,
'Enchantress':58,
'Huskar':59,
'Night Stalker':60,
'Broodmother':61,
'Bounty Hunter':62,
'Weaver':63,
'Jakiro':64,
'Batrider':65,
'Chen':66,
'Spectre':67,
'Ancient Apparition':68,
'Doom':69,
'Ursa':70,
'Spirit Breaker':71,
'Gyrocopter':72,
'Alchemist':73,
'Invoker':74,
'Silencer':75,
'Outworld Devourer':76,
'Lycan':77,
'Brewmaster':78,
'Shadow Demon':79,
'Lone Druid':80,
'Chaos Knight':81,
'Meepo':82,
'Treant Protector':83,
'Ogre Magi':84,
'Undying':85,
'Rubick':86,
'Disruptor':87,
'Nyx Assassin':88,
'Naga Siren':89,
'Keeper of the Light':90,
'Io':91,
'Visage':92,
'Slark':93,
'Medusa':94,
'Troll Warlord':95,
'Centaur Warrunner':96,
'Magnus':97,
'Timbersaw':98,
'Bristleback':99,
'Tusk':100,
'Skywrath Mage':101,
'Abaddon':102,
'Elder Titan':103,
'Legion Commander':104,
'Techies':105,
'Ember Spirit':106,
'Earth Spirit':107,
'Underlord':108,
'Terrorblade':109,
'Phoenix':110,
'Oracle':111,
'Winter Wyvern':112}

coefmatrix = (1.23454395303285 ,  1.16182142473777 ,  1.2703225022877 ,   1.14627211229078 ,  1.60140683835123 ,  1.35020949419738 ,  1.42994193650351 
    ,  1.38764351927468 ,  1.48337191929531 ,  1.01975753492294 ,  1.31589145156114 ,  1.23332317458786 ,  0.933560893405223 , 1.35985657204192 
    ,  1.26144851933923 ,  1.30359928443253 ,  0.879909075638846 , 1.44741265472389 ,  1.30621201816178 ,  1.50766206060722 ,  1.24443233757443 
    ,  1.58449227893762 ,  1.2567821842343 ,   0 , 1.0646682980741 ,   1.31707743432279 ,  1.58359795901165 ,  1.62027310041561 ,  1.33431000068961 
    ,  1.46784718909303 ,  1.64025436952536 ,  1.6733468274447 ,   1.33258143728099 ,  1.01322983200102 ,  1.07232524083444 ,  1.69017264727538 
    ,  1.63097336321114 ,  1.38722666453237 ,  1.1150589544279 ,   1.46229362420192 ,  1.12729877551744 ,  1.67982265817497 ,  1.34532170863488 
    ,  1.2121591346664 ,   1.24366455421886 ,  1.34625366422953 ,  1.33519808738595 ,  1.50976890499098 ,  1.36929486828462 ,  1.53582090448921 
    ,  1.33764189363163 ,  1.19342710491093 ,  0.947409034809793 , 1.22270552217879 ,  1.390430431145 ,    1.29875416961237 ,  1.82132292549979 
    ,  1.03193242479797 ,  1.17237778081953 ,  1.48452575567122 ,  0.951318073178483 , 1.43544249642843 ,  1.2371037904689 ,   1.44019078275556 
    ,  1.13811636961102 ,  1.31344069478402 ,  1.72880424040759 ,  1.46978095761508 ,  1.5449710092793 ,   1.6132353874073 ,   1.54486399153952 
    ,  1.30526693971516 ,  1.39906988586347 ,  1.25910274219761 ,  1.54136330508932 ,  1.15712994323718 ,  1.35527547187674 ,  1.32982130030252 
    ,  0.992779983461705 , 0.958090309287318 , 1.38247369733918 ,  1.10548559482569 ,  1.50886456641502 ,  1.53836383210442 ,  1.70119626624154 
    ,  1.24588248063528 ,  1.51508070818495 ,  1.31223821268185 ,  1.13520746973913 ,  1.23327570054309 ,  1.24642371783198 ,  1.4245019900164 
    ,   1.28947950636753 ,  1.40915676828533 ,  1.29364113006649 ,  1.46450595014547 ,  1.15544343537953 ,  1.20275807640301 ,  1.26252947302184 
    ,  1.46721043221923 ,  1.12510668977442 ,  1.75824419882627 ,  1.36102647152053 ,  1.34362366228017 ,  1.2113140377886 ,   1.27019542715577 
    ,  1.44679865642176 ,  0 , 1.42852977323597 ,  1.48301766175982 ,  1.31643013256682 ,  1.45768151969721 ,  0.235397644528861 , 0.331729615057013 
    , 0.162588130108987 , 0.29888470774359 ,  -0.0648128771958832 ,   -0.000767758683272263 , 0.0239122696693534 ,    -0.0222428235268095 
    ,   -0.00545022145009522 ,  0.35049270121034 ,  0.133034739876247 , 0.314007849640513 , 0.452206812920442 , 0.138044658065818 , 0.289646403425705 
    , 0.156819045088344 , 0.48794491364668 ,  0.0529994378099652 ,    0.219458145612298 , -0.0943197412040337 ,   0.234527993405337 , -0.0388343612384171 
    ,   0.322510009966649 , 0 , 0.43836753219312 ,  0.183643551518555 , 0.0216037620688482 ,    -0.19825709736085 , 0.0361456095354126 ,    0.0106391046339932 
    ,    -0.196832471082076 ,    -0.122829696536552 ,    0.0497793350754742 ,    0.36065263722863 ,  0.383759257535162 , -0.150151532069239 ,    -0.0391550107273752 
    ,   -0.135030236091936 ,    0.42096700420119 ,  -0.0590855702309353 ,   0.319970324828321 , -0.238461262296262 ,    0.15792493507902 ,  0.234937528514651 
    , 0.0851743998111874 ,    0.20420431172757 ,  0.102208632610755 , 0.112690245663498 , 0.130856373027173 , -0.074437216822003 ,    0.0552225018813691 
    ,    0.268163626009629 , 0.420130156482559 , 0.260372636167979 , -0.0370425949568814 ,   0.228791276325226 , -0.366451227505184 ,    0.477482409721693 
    , 0.0775322798303618 ,    0.0165732802114812 ,    0.358286426616556 , 0.0538684712900154 ,    0.278986692353062 , 0.00295071207566925 ,   0.323977607627623
    , 0.181650198076148 , -0.207229539429467 ,    0.0571492235226357 ,    -0.0895667628668503 ,   -0.261869982208006 ,    -0.128947567735263 ,    0.0838736140317823 
    ,    0.0387671472860309 ,    0.18150038849395 ,  0.00417225957345187 ,   0.290509486133934 , -0.0530295729053097 ,   0.0974392382651124 ,    0.37815715987679 
    ,  0.215124373280029 , 0.0725059230641893 ,    0.141624179182744 , -0.0584956222475652 ,   0.00824835163194758 ,   -0.193186978061132 ,    0.232155546422942 
    , -0.062797173049113 ,    0.154669048856521 , 0.24559932483257 ,  0.0652780779978316 ,    0.266720475297926 , 0.130608864021112 , 0.109355607056511 , 0.0136239922149848 
    ,    0.191245972549135 , -0.0205700842302285 ,   0.328584756307223 , 0.322927942557564 , 0.151548128946827 , 0.0580838712853496 ,    0.296616494699377 , -0.218168996434478 
    ,    -0.0912329206697045 ,   0.226653747637939 , 0.221771624639237 , 0.283566971374919 , -0.0650148436094005 ,   0 , 0.0317403174958671 ,    -0.0365357517055045 ,   0.164242603682135 , 0)



@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    test.append(request.form['Player1'])
    test.append(request.form['Player2'])
    test.append(request.form['Player3'])
    test.append(request.form['Player4'])
    test.append(request.form['Player5'])
    test.append(request.form['Player6'])
    test.append(request.form['Player7'])
    test.append(request.form['Player8'])
    test.append(request.form['Player9'])
    test.append(request.form['Player10'])


    #processed_text = text
    #text = 'dog'
    return redirect(url_for("hello"))


@app.route('/Result', methods=['GET'])
def hello():
    global counter
    global compare
    global test

    if counter > compare:
        i = 0
        while i < 10:
            del test[0]
            i += 1

    counter = counter + 1
    print(len(array2))

    index = dictionary.get(test[0]) 
    array2[index] = 1

    index = dictionary.get(test[1]) 
    array2[index] = 1

    index = dictionary.get(test[2]) 
    array2[index] = 1

    index = dictionary.get(test[3]) 
    array2[index] = 1

    index = dictionary.get(test[4]) 
    array2[index] = 1

    index = dictionary.get(test[5]) 
    array2[index+112] = 1

    index = dictionary.get(test[6]) 
    array2[index+112] = 1

    index = dictionary.get(test[7]) 
    array2[index+112] = 1

    index = dictionary.get(test[8]) 
    array2[index+112] = 1

    index = dictionary.get(test[9]) 
    array2[index+112] = 1


    global calculatedvalue
    calculatedvalue = 0
    global intercept
    print(calculatedvalue)
    for i in range(0,224):
        calculatedvalue = calculatedvalue + coefmatrix[i]*array2[i]

    number = 1/(1+math.exp(-calculatedvalue-intercept))
    number =  number * 100


    
    return render_template('result.html',number = number)




@app.route('/Result')
def back():
    return redirect(url_for("my_form"));



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debut=True)
#print (my_form_post())

