import pyperclip


def descGen(heading, paragraphs):
    result = f'<h4>{heading}</h4>'
    for paragraph in paragraphs:
        result += f'<p>{paragraph}</p>'
    return result


def nameGen(nametype, names):
    return f'<span class="feature">{nametype} Names:</span>{names}<br />'


def traitGen(traitName, traitDescription):
    return f'<p class="indent"><strong><em>{traitName}</em></strong>{traitDescription}</p>'


def nameSetterGen(nametype, names):
    return f'<set name="names" type="{nametype.lower()}">{names}</set>'


def statGen(stat, statValue, subraceStat=False):
    result = f'<stat name="{stat}" value="{statValue}"'
    if not subraceStat:
        result += f' requirements="!ID_ORKIDIAN_INTERNAL_SUB_RACE"'
    return result + '/>'


def traitGrantGen(traitName):
    return f'<grant type="Racial Trait" id="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{traitName.upper().replace(" ", "_")}" />'


def tableGen(tableName, tableDescription, tableOptions):
    result = f'<element name="{tableName}" type="Racial Trait" source="League of Legends Handbook" id="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{tableName.upper().replace(" ", "_")}"><description>{tableDescription}</description><rules><select type="Racial Trait" name="{tableName}" supports="{tableName}" /></rules></element>'

    for (tableTrait, tableTraitDesc) in tableOptions:
        result += f'<element name="{tableName} ({tableTrait})" type="Racial Trait" source="League of Legends Handbook" id="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{tableName.upper().replace(" ", "_")}_{tableTrait.upper().replace(" ", "_")}"><supports>{tableName}</supports><description><div element="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{tableName.upper().replace(" ", "_")}" /></description><sheet alt="{tableTrait}"><description>{tableTraitDesc}</description></sheet><rules></rules></element>'

    return result

# {
# "name":,
#  "desc":,
# "traitDescs":[],
# "traits":[],
# "stats":[]
# }


def subraceGen(subrace, name):
    result = f'<element name="{subrace["name"].strip()} {name}" type="Sub Race" source="League of Legends Handbook" id="ID_ORKIDIAN_LOLHB_SUB_RACE_{subrace["name"].strip().upper().replace(" ", "_")}"><supports>{name}</supports><description>{subrace["desc"]}'

    for (traitName, traitDescription) in subrace["traitDescs"]:
        result += traitGen(traitName, traitDescription)

    result += f'</description><sheet display="false" /><setters><set name="height" modifier="'

    try:
        result += f'{subrace["hm"]}">'
    except KeyError:
        result += f'2d10'

    result += f'">'

    try:
        result += f'{subrace["h"]}">'
    except KeyError:
        result += f'4\'8"'

    result += f'</set><set name="weight" modifier="'

    try:
        result += f'{subrace["wm"]}">'
    except KeyError:
        result += f'2d4'

    result += f'">'

    try:
        result += f'{subrace["w"]}">'
    except KeyError:
        result += f'110 lb.'

    result += f'</set></setters><rules><grant type="Feat" id="ID_ORKIDIAN_INTERNAL_SUB_RACE" />'

    try:
        for (traitName2, traitDescription2) in subrace["traits"]:
            result += traitGrantGen(traitName2)
    except KeyError:
        pass

    try:
        for (stat, statValue) in subrace["stats"]:
            result += statGen(stat, statValue, True)
    except KeyError:
        pass

    result += f'</rules></element>'

    try:
        for (traitName2, traitDescription2) in subrace["traits"]:
            result += traitElementGen(traitName2, traitDescription2)
    except KeyError:
        pass

    return result


def traitElementGen(traitName, traitDesc):
    return f'<element name="{traitName}" type="Racial Trait" source="League of Legends Handbook" id="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{traitName.upper().replace(" ", "_")}"><description><p>{traitDesc}</p></description><sheet><description>{traitDesc}</description></sheet><rules></rules></element>'


def raceGen(name, flavor, descriptions,
            # Names
            nameDescription, namesData, nameFormat,
            # Traits & stats
            traitsDescription, traits, traitsDescriptions, stats, multistat=None, multistatAmount=0,
            # Height and weight, speed, size, darkvision
            height="4'8\"", heightMod="2d10", weight="110 lb", weightMod="2d4",
            speed="30", size="medium", darkvision=False,
            # Languages
            manyLanguages=None,
            # Subraces
            subraces=None, subraceDescription=None,
            # Table/AdditionalStrings
            tableName=None, tableDesc=None, tableOptions=None, additionalStrings=""
            ):
    result = f'<?xml version="1.0" encoding="utf-8" ?><elements><info><name>{name}</name><update version="0.0.1"><file name="race-{name}.xml" url="" /></update></info><element name="{name}" type="Race" source="League of Legends Handbook" id="ID_ORKIDIAN_LOLHB_RACE_{name.upper().replace(" ", "_")}"><description><p class="flavor">{flavor}</p>'

    for (heading, paragraphs) in descriptions:
        result += descGen(heading, paragraphs)

    result += f'<h4>{name} names</h4><p>{nameDescription}</p><p>'

    for (nametype, names) in namesData:
        result += nameGen(nametype, names)

    result += f'</p><h4>{name} traits</h4><p>{traitsDescription}</p>'

    for (traitName, traitDescription) in traitsDescriptions:
        result += traitGen(traitName, traitDescription)

    result += f'</description><sheet display="false" /><setters>'

    for (nametype, names) in namesData:
        nameSetterGen(nametype, names)

    result += f'<set name="names-format">{nameFormat}</set><set name="height" modifier="{heightMod}">{height}</set><set name="weight" modifier="{weightMod}">{weight}</set></setters><rules>'

    for (stat, statValue) in stats:
        statGen(stat, statValue)

    if multistat:
        result += f'<select type="Racial Trait" name="Ability Score Increase ({name})" supports="{name}" number="{multistatAmount}" requirements="!ID_ORKIDIAN_INTERNAL_SUB_RACE"/>'

    result += f'<stat name="innate speed" value="{speed}" bonus="base"/><grant type="Size" id="ID_SIZE_{size.upper()}" />'

    if(darkvision):
        result += f'<grant type="Vision" id="ID_VISION_DARKVISION" />'

    result += '<grant type="Language" id="ID_ORKIDIAN_LOLHB_LANGUAGE_VANOX" />'

    if(manyLanguages):
        result += f'<select type="Language" name="Language ({name})" supports="Standard||Exotic" number={manyLanguages} requirements="!ID_ORKIDIAN_INTERNAL_SUB_RACE"/>'

    for (traitName, traitDescription) in traits:
        result += traitGrantGen(traitName)

    if subraces:
        result += f'<grant type="Racial Trait" id="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{name.upper().replace(" ", "_")}_SUBRACE" />'

    result += f'</rules></element>'

    for (traitName, traitDescription) in traits:
        result += traitElementGen(traitName, traitDescription)

    if tableName:
        result += tableGen(tableName, tableDesc, tableOptions)

    if subraces:
        result += f'<element name="{name} Subrace" type="Racial Trait" source="League of Legends Handbook" id="ID_ORKIDIAN_LOLHB_RACIAL_TRAIT_{name.upper().replace(" ", "_")}_SUBRACE"><description><p>{subraceDescription}</p></description><sheet display="false" /><rules><select type="Sub Race" name="{name} Subrace" supports="{name}" /></rules></element>'
        for subrace in subraces:
            result += subraceGen(subrace, name)

    result += f'{additionalStrings}</elements>'
    return result


additionalStrings = ""
# for (trait, traitDesc) in [
#     ("Blood Magic", "The Darkin created and perfected the arcane power of blood magic, called hemomancy. As a bonus action, you can use this knowledge to heal your wounds for 1d6 + CHA hit points. After you use this feature, you can’t use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes a d10 at 5th level, a d12 at 10th level, and a d20 at 15th level."),
#     ("Sealed Weapon", "All existing Darkin are inseparably tied to their weapon of choice. You are proficient in this weapon. In order to roam the world, the Darkin requires a mortal to take hold of the weapon and become their host. In doing so, the host's mind and identity are erased, and their body becomes possessed by the Darkin. The weapon must remain within 10 feet of the Darkin at all times. Without a host, the Darkin’s consciousness is plunged in darkness, without the ability to see or feel until another mortal attempts to wield them."),
#     ("Vengeance of the Darkin", "The Darkin have an appetite for bloodshed; using your sealed weapon, you can critically hit on a 19 or 20. When you critically hit with the sealed weapon, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.")
# ]:
#     additionalStrings += traitElementGen(trait, traitDesc)

# additionalStrings += tableGen("Blessing of the Sun Disc", "<p>The transformation has gifted you with a unique ability based on the studies and nature of your life as a human. Select one from the list below or work with the DM to craft a blessing of similar power:</p><table><thead><tr><th>Blessing</th><th>Description</th></tr></thead><tbody><tr><th>Ascended Fury</th><td><p>When successfully landing an attack that deals bludgeoning, piercing, or slashing damage, you can channel Ascended Fury to cause that attack to deal another 1d6 + STR damage. After using this blessing, you can't use it again until you complete a long rest.</p><p>This damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 1d12 at 10th level, and a 2d12 at 15th level.</p></td></tr><tr><th>Ghost of the Soldier</th><td><p>As a bonus action, you can conjure a Sand Soldier within 15 feet of you and in an empty space with 5 feet on all sides.<ul><li>It can make a melee spear attack for 1d6 + DEX.</li><li>Your movement can be used to move the soldier.</li><li>The soldier cannot perceive anything.</li><li> The soldier has hit points equal to 1d6 + CHA.</li><li>The soldier dissolves after 1 minute or if you are not within 15 feet of it.</li></ul>After using this blessing, you can't use it again until you complete a long rest.</p><p>The damage die changes when you reach certain levels. The die becomes 2d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p></td></tr><tr><th>Life Siphon</th><td><p>As an action, roll 1d6 + CHA against a creature you can see. You take this amount of hit points away from the target and add it to your own. The target may make a DC 13 CON saving throw to resist, losing half the amount of hit points on a successful save. This has no effect on Constructs or Undead. After using this blessing, you can't use it again until you complete a long rest.</p><p>The damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p></td></tr></tbody></table>",
#                               [("Ascended Fury", "<p>When successfully landing an attack that deals bludgeoning, piercing, or slashing damage, you can channel Ascended Fury to cause that attack to deal another 1d6 + STR damage. After using this blessing, you can't use it again until you complete a long rest.</p><p>This damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 1d12 at 10th level, and a 2d12 at 15th level.</p>"), ("Ghost of the Soldier", "<p>As a bonus action, you can conjure a Sand Soldier within 15 feet of you and in an empty space with 5 feet on all sides.<ul><li>It can make a melee spear attack for 1d6 + DEX.</li><li>Your movement can be used to move the soldier.</li><li>The soldier cannot perceive anything.</li><li> The soldier has hit points equal to 1d6 + CHA.</li><li>The soldier dissolves after 1 minute or if you are not within 15 feet of it.</li></ul>After using this blessing, you can't use it again until you complete a long rest.</p><p>The damage die changes when you reach certain levels. The die becomes 2d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p>"), ("Life Siphon", "<p>As an action, roll 1d6 + CHA against a creature you can see. You take this amount of hit points away from the target and add it to your own. The target may make a DC 13 CON saving throw to resist, losing half the amount of hit points on a successful save. This has no effect on Constructs or Undead. After using this blessing, you can't use it again until you complete a long rest.</p><p>The damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p>")])

# additionalStrings += tableGen("Blessing of the Aspect", "Scaling Mount Targon has convinced an Aspect to grant you their power. Consider your bond with this Aspect; have they bestowed you a shred of their abilities? Or have they fully merged with you, erasing your previous identity? Select one from the list or work with the DM to craft a blessing of similar power:<table><thead><tr><th>Blessing</th><th>Description</th></tr></thead><tbody><tr><td>Aspect of Destiny</td><td>While out of combat, you may use this blessing to alter the threads of fate. Predict and describe events of the next three in-game minutes. The DM can determine if these events will be Easy (DC 10), Medium (DC 13), Hard (DC 17), or Impossible (DC 20) to occur. Then, roll 1d20. On a successful role, events happen as described. After using this blessing (on a success or fail), you can't use it again until you complete a short or long rest.</td></tr><tr><td>Aspect of Health</td><td>As an action, you may invoke your Aspect to heal yourself or another willing creature you see for 1d6 + CHA. After using this blessing, you can't use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes 1d10 at 5th level, 1d12 at 10th level, and 2d12 at 15th level.</td></tr><tr><td>Aspect of the Messenger</td><td>You can establish a link of telepathic communication between yourself and any creature or entity that you have met before, across any distance. They must be able to comprehend a language you share. The link lasts for 5 minutes. In order to maintain the link, the rules of Concentration apply. After using this blessing, you can't use it again until you complete a long rest.</td></tr><tr><td>Aspect of Revelry</td><td>When prompted to make a Charisma check, you can use this blessing to add +10 to the roll. After using this blessing, you can't use it again until you complete a long rest.</td></tr></tbody></table>",
#                               [
#                                   ("Aspect of Destiny", "While out of combat, you may use this blessing to alter the threads of fate. Predict and describe events of the next three in-game minutes. The DM can determine if these events will be Easy (DC 10), Medium (DC 13), Hard (DC 17), or Impossible (DC 20) to occur. Then, roll 1d20. On a successful role, events happen as described. After using this blessing (on a success or fail), you can't use it again until you complete a short or long rest."),
#                                   ("Aspect of Health", "As an action, you may invoke your Aspect to heal yourself or another willing creature you see for 1d6 + CHA. After using this blessing, you can't use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes 1d10 at 5th level, 1d12 at 10th level, and 2d12 at 15th level."),
#                                   ("Aspect of the Messenger", "You can establish a link of telepathic communication between yourself and any creature or entity that you have met before, across any distance. They must be able to comprehend a language you share. The link lasts for 5 minutes. In order to maintain the link, the rules of Concentration apply. After using this blessing, you can't use it again until you complete a long rest."),
#                                   ("Aspect of Revelry", "When prompted to make a Charisma check, you can use this blessing to add +10 to the roll. After using this blessing, you can't use it again until you complete a long rest.")
#                               ])
# pyperclip.copy(raceGen(name="Ascended",
#                        flavor="Transformed by an ancient, divine disc or merged with a celestial power, the Ascended are elevated beyond their mortal states into legendary, powerful beings. Physically, they are indelibly evolved, made more powerful, more swift, and more resilient. Their minds are changed as well; indeed, due to their exalted station, they are concerned with matters far above the day-to-day matters of mortals. From protecting the noble tenets of justice and truth to pursuing world-ending revenge, the nature of an individual Ascended depends on their life as a mortal and the nature of their Ascension. No matter the motivation, the presence of an Ascended points to universe-altering events to come.",
#                        descriptions=[("Beyond Mortal Bounds", ["Extremely rare, the Ascended are some of the most powerful beings to roam Runeterra. With inhuman speed, strength, and stamina, the Ascended are called to commit themselves to otherworldly, far-reaching causes.", "The physical form of such a being shows undeniable evidence of their Ascension. The Shuriman Ascended fuse with the image of an animal, assuming a beastly and noble quality. The Targonian Ascended, though human in likeness, may have characteristics that reveal the celestial that resides within them. For instance, Leona, the Aspect of the Sun, seems to physically shine with the power of the Sun, and her eyes burn with its brightness. The Darkin warp the bodies of their mortal hosts, slowly decaying the form through corrupt energy and blood magic.",
#                                                                "Although immune to most natural causes of death, the Ascended can be defeated in some manner. Particular weapons and magics exist that can maim or kill Shuriman and Targonian Ascended, and the Darkin can be sealed within their weapons so long as they are without a host."])],
#                        nameDescription="As both the Shuriman Ascended and the Darkin reached Ascension during the reign of the Shuriman Empire, their names are based in the Ancient Shuriman language. The Darkin, according to their leader Aatrox, frequently have doubled vowels in their names. The Targonian Ascended tend to keep their mortal, mundane names rather than assume the identity of the celestial aspect within them (see Targonian Humans).",
#                        namesData=[
#                            ("Shuriman", "Az'ravi, Bahatek, Esh'kai, Ishtaka, Nacrath, Nixa, Retekta, Sek'riza, Xeyush"), ("Darkin",
#                                                                                                                           "Aalrut, Ceheltox, Khaal, Ma'almar, Nek'xast, Rhelaas, Seltaava, Shalteeya, Taltarus, Virresh, Xuust")
#                        ],
#                        traitsDescription="Your Ascended character has the following traits:",
#                        traitsDescriptions=[
#                            ("Ability Score Increase",
#                             "Your Dexterity score increases by 2."),
#                            ("Age", "Prior to becoming Ascended, these beings age according to their mortal life. After Ascension, their aging slows and their natural lifespans are drastically increased, spanning millennia."),
#                            ("Alignment", "The Ascended are steadfast in their ambitions; without personal appetite and vigor, their Ascension would undoubtedly fail. As such, they are rarely of totally neutral alignments. Targonian Ascended tend toward good alignments, while Darkin tend toward evil."),
#                            ("Size", "Some retain their human frame when becoming Ascended, and others are altered in size and shape after the transformation. As such, Ascended vary from about 5 feet to over 7 feet tall. Your size is Medium."),
#                            ("Speed", "Your base walking speed is 30 feet."),
#                            ("Ascended Endurance", "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest."),
#                            ("Languages", "You can speak, read, and write Va-Nox."),
#                            ("Subrace", "The different processes of Ascension divides the Ascended into Shuriman Ascended and Targonian Ascended. From there, the Darkin are formerly Shuriman Ascended who have been corrupted through war and betrayal. Choose one of these subraces.")
#                        ],
#                        subraceDescription="The different processes of Ascension divides the Ascended into Shuriman Ascended and Targonian Ascended. From there, the Darkin are formerly Shuriman Ascended who have been corrupted through war and betrayal. Choose one of these subraces.",
#                        traits=[("Ascended Endurance", "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.")],
#                        subraces=[{"name": "Shuriman",
#                                   "desc": '''<p>Millennia ago, during the height of the Shuriman Empire, Shuriman warriors of exceptional loyalty and ability had been selected for a rite known as the Ritual of Ascension. Through the power of an ancient, colossal artifact known as the Sun Disc of Shurima, these warriors had been imbued with mystic energy.Based on the ideals they uphold and Shurima's culture of symbolism, they are merged with an aligning animalistic spirit. These beings harbor great physical strength, stature, and resilience. Indeed, when the sun had not yet set on the Empire of Shurima, these beings made up an Ascended legion, the Sunborn, charged with protecting Shurima and Azir.</p>
# <p>In the days of the empire's decline, the Ritual of Ascension had failed with greater frequency. Unsuccessful Ascensions either killed those who participated in the ceremony or produced failed, scarred Ascended called Baccai. Furthermore, most of the Ascended of ancient times had been destroyed in battles with the Void and in civil wars. Nonetheless, the recent resurrection of the Shuriman emperor Azir and his following Ascension reveals that the</p>
# <p>Sun Disc may yet claim the worthy for its sacred transformation.</p>''',
#                                   "traitDescs": [
#                                       ("Ability Score Increase", "Your Constitution score increases by 1."), ("Blessing of the Sun Disc", '''<p>The transformation has gifted you with a unique ability based on the studies and nature of your life as a human. Select one from the list below or work with the DM to craft a blessing of similar power:</p><table><thead><tr><th>Blessing</th><th>Description</th></tr></thead><tbody><tr><th>Ascended Fury</th><td><p>When successfully landing an attack that deals bludgeoning, piercing, or slashing damage, you can channel Ascended Fury to cause that attack to deal another 1d6 + STR damage. After using this blessing, you can't use it again until you complete a long rest.</p><p>This damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 1d12 at 10th level, and a 2d12 at 15th level.</p></td></tr><tr><th>Ghost of the Soldier</th><td><p>As a bonus action, you can conjure a Sand Soldier within 15 feet of you and in an empty space with 5 feet on all sides.<ul><li>It can make a melee spear attack for 1d6 + DEX.</li><li>Your movement can be used to move the soldier.</li><li>The soldier cannot perceive anything.</li><li> The soldier has hit points equal to 1d6 + CHA.</li><li>The soldier dissolves after 1 minute or if you are not within 15 feet of it.</li></ul>After using this blessing, you can't use it again until you complete a long rest. </p><p>The damage die changes when you reach certain levels. The die becomes 2d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p></td></tr><tr><th>Life Siphon</th><td><p>As an action, roll 1d6 + CHA against a creature you can see. You take this amount of hit points away from the target and add it to your own. The target may make a DC 13 CON saving throw to resist, losing half the amount of hit points on a successful save. This has no effect on Constructs or Undead. After using this blessing, you can't use it again until you complete a long rest.</p><p>The damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p></td></tr></tbody></table>'''),
#                                       ("Desert Terrain Familiarity",
#                                        "When traveling in desert terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain."),
#                                       ("Extra Languages",
#                                        "You can speak, read, and write in Ancient Shuriman and Modern Shuriman.")
#                                   ],
#                                   "traits":[
#                                       ("Blessing of the Sun Disc", 'DELETE THIS'),
#                                       ("Desert Terrain Familiarity", "When traveling in desert terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.")
#                                   ],
#                                   "stats":[("dexterity", 2),
#                                            ("constitution", 1)]
#                                   }, {
#                            "name": "Targonian ",
#                            "desc": '''<p>The peak of Mount Targon exudes celestial power. The apex is the apparent portal between the physical world and Targon Prime, a celestial realm where beings known as Aspects live. But the mountain is nigh impossible to scale. Hidden by a layer of clouds, its rocky paths shift constantly—the land itself altered by a higher magic. Even reaching the top of the mountain is not a guarantee of one's success. Some may find empty ruins at the mountaintop, reflecting their soul's unworthiness. The ascent is the ultimate challenge of one's endurance, skill, dedication, and spirit.</p>
# <p>Most mortals lose their lives in the climb. But for the few that make it—and for the fewer that the mountain finds worthy—they are rewarded with heavenly magic. The stellar Aspects, who embody concepts and constellations, may bestow some of their power unto a deserving mortal. Or, the Aspect may even fuse with a mortal, leaving the celestial plane and elevating the mortal into an almighty host.</p>''',
#                            "traitDescs": [("Ability Score Increase", "Your Charisma score increases by 1."),
#                                           ("Blessing of the Aspect", '''Scaling Mount Targon has convinced an Aspect to grant you their power. Consider your bond with this Aspect; have they bestowed you a shred of their abilities? Or have they fully merged with you, erasing your previous identity? Select one from the list or work with the DM to craft a blessing of similar power:
# <table>
#     <thead>
#         <tr>
#             <th>Blessing</th>
#             <th>Description</th>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Aspect of Destiny</td>
#             <td>While out of combat, you may use this blessing to alter the threads of fate. Predict and describe events of the next three in-game minutes. The DM can determine if these events will be Easy (DC 10), Medium (DC 13), Hard (DC 17), or Impossible (DC 20) to occur. Then, roll 1d20. On a successful role, events happen as described. After using this blessing (on a success or fail), you can't use it again until you complete a short or long rest.</td>
#         </tr>
#         <tr>
#             <td>Aspect of Health</td>
#             <td>As an action, you may invoke your Aspect to heal yourself or another willing creature you see for 1d6 + CHA. After using this blessing, you can't use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes 1d10 at 5th level, 1d12 at 10th level, and 2d12 at 15th level.</td>
#         </tr>
#         <tr>
#             <td>Aspect of the Messenger</td>
#             <td>You can establish a link of telepathic communication between yourself and any creature or entity that you have met before, across any distance. They must be able to comprehend a language you share. The link lasts for 5 minutes. In order to maintain the link, the rules of Concentration apply. After using this blessing, you can't use it again until you complete a long rest.</td>
#         </tr>
#         <tr>
#             <td>Aspect of Revelry</td>
#             <td>When prompted to make a Charisma check, you can use this blessing to add +10 to the roll. After using this blessing, you can't use it again until you complete a long rest.</td>
#         </tr>
#     </tbody>
# </table>'''),
#                                           ("Extra Language",
#                                            "You can speak, read, and write in Targonian."),
#                                           ("Mountainous Terrain Familiarity", "When traveling in mountainous terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.")],
#                            "traits": [("Mountainous Terrain Familiarity", "When traveling in mountainous terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain."), ("Blessing of the Aspect", "DELETE THIS")],
#                            "stats": [("dexterity", 2), ("charisma", 1)]
#                        }, {
#                            "name": "Darkin",
#                            "desc": "<p>Once god-warriors in the Ascended legion of the ancient Shuriman Empire, the Darkin are Ascended who have fallen far from grace. Several horrors and betrayals led to their irreversible corruption.</p><p>Fighting off the Void from consuming Runeterra exposed them to unspeakable abominations and catastrophic brutality. The fall of the emperor Azir and the collapse of the empire caused infighting in the Ascended legion, leaving many to feel purposeless, adrift. In this conflict between the Ascended, known as the Darkin War, those that would become the Darkin developed blood magic, forming and reforming their bodies. This war raged over Runeterra, with the Darkin taking countless mortal lives to fuel their magic and heal their wounds.</p><p>But ultimately, the Darkin were sealed away due to the intervention of the Targonians, particularly the Aspect of Twilight, a Targonian Ascended. The Aspect of Twilight taught mortals the magic necessary to entrap Darkin beings within their own weapons, if not outright destroyed. The Darkin War ended with the Darkin being suppressed and scattered; as centuries passed, the knowledge of their world-ending existence and capabilities fell into obscurity. But in recent times, mortals have found these once-hidden weapons and sought to wield them—potentially reviving these apocalyptic beings. When a mortal picks up a Darkin weapon, they are almost always instantly destroyed, their body overtaken and morphed into the Darkin’s physical host.</p>",
#                            "traitDescs": [("Ability Score", "Increase Your Strength score increases by 1."),
#                                           ("Blood Magic", "The Darkin created and perfected the arcane power of blood magic, called hemomancy. As a bonus action, you can use this knowledge to heal your wounds for 1d6 + CHA hit points. After you use this feature, you can’t use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes a d10 at 5th level, a d12 at 10th level, and a d20 at 15th level."),
#                                           ("Sealed Weapon", "All existing Darkin are inseparably tied to their weapon of choice. You are proficient in this weapon. In order to roam the world, the Darkin requires a mortal to take hold of the weapon and become their host. In doing so, the host's mind and identity are erased, and their body becomes possessed by the Darkin. The weapon must remain within 10 feet of the Darkin at all times. Without a host, the Darkin’s consciousness is plunged in darkness, without the ability to see or feel until another mortal attempts to wield them."),
#                                           ("Vengeance of the Darkin", "The Darkin have an appetite for bloodshed; using your sealed weapon, you can critically hit on a 19 or 20. When you critically hit with the sealed weapon, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit."),
#                                           ("Extra Languages", "You can speak, read, and write in Ancient Shuriman and the native language of your mortal host.")],
#                            "traits": [("Blood Magic", "The Darkin created and perfected the arcane power of blood magic, called hemomancy. As a bonus action, you can use this knowledge to heal your wounds for 1d6 + CHA hit points. After you use this feature, you can’t use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes a d10 at 5th level, a d12 at 10th level, and a d20 at 15th level."),
#                                       ("Sealed Weapon", "All existing Darkin are inseparably tied to their weapon of choice. You are proficient in this weapon. In order to roam the world, the Darkin requires a mortal to take hold of the weapon and become their host. In doing so, the host's mind and identity are erased, and their body becomes possessed by the Darkin. The weapon must remain within 10 feet of the Darkin at all times. Without a host, the Darkin’s consciousness is plunged in darkness, without the ability to see or feel until another mortal attempts to wield them."),
#                                       ("Vengeance of the Darkin", "The Darkin have an appetite for bloodshed; using your sealed weapon, you can critically hit on a 19 or 20. When you critically hit with the sealed weapon, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.")],
#                            "stats": [("dexterity", 2), ("strength", 1)]
#                        }], nameFormat="{{name}}", stats=[("dexterity", 2)], additionalStrings=additionalStrings))

# pyperclip.copy(raceGen(name="Celestial",
# flavor="Old as the universe and just as powerful, Celestials cross the boundaries of mortal possibility. With vast ranges of abilities, such as the power of creation, healing, or omniscience, Celestials demonstrate great providence over the physical realm. However, most Celestials are inhuman, bordering on eldritch in appearance, utterly disconnected from the mortals they ostensibly oversee. While most Celestials choose to remain in the Celestial Realm, content in their incomprehensibility, a select few decide to descend into the mortal realm. But these Celestials almost never come in their pure, godlike forms. Instead, they typically sacrifice some condition of their sublimity in order to better interact with mortals. Or, they may even imbue their essence within mortals, merging with someone worthy and willing.",
# descriptions=[("Hands of Fate", ["Celestials are the weavers of destiny, with the power to guide fate toward its course. From the domain of the Celestial Realm, fully-powered Celestials exercise the breadth of their influence. Celestials, knowledgable in the different threads of fate, aim their efforts in preserving the multiverse's longevity. This might be interpreted as goodness or benevolence, but it is perhaps more accurate to acknowledge Celestial actions as being beyond mortal grasp. Indeed, some Celestials pursue more ambivalent strands and developments, such as creating change for change's sake."]),
# ("Aspects and Visionaries",["A specific type of Celestial exists, residing and originating in a plane called Targon Prime, known as Aspects. The Aspects personify a concept, such as war, justice, or change. These concepts evolve through mortal affairs. At times that necessitate widespread transformation, or if a mortal proves themselves worthy in the ritual of Ascension, an Aspect comes down and merges with a mortal. In this form, an Aspect can be destroyed by a being of equal power, or the Aspect may choose a different mortal host."]),("Humanity's Guardians", ["Some mortal faiths are based in the worship of Celestials. But most followers have not born witness to an actual Celestial, nor have they seen their direct influence. Nonetheless, Celestials may take a hands-on or hands-off approach to helping humans. Stories around Mount Targon spread of a Celestial who sacrificed her immortal, animalistic form and exchanged it for corporeality—embracing all the weaknesses of humanity to better serve them. For all the cruelty of mortals, it seems there are entities dedicated to saving them."]),("Stellar Influence", ["Celestial agency takes different forms. The mythos of the creation of the Ascended claims that Celestials made them as weapons against the Void's corruption. Another type of Celestial exists, called Celestial dragons. These beings manipulate the stars and suns themselves. These dragons may explain the existence of celestial bodies and universes as creations by a higher being. In either case, Celestial power seems tied to the stars, and thus Celestials have appointed themselves as the guardians of all that the stars cover."])],
# nameDescription="Celestial names are based in the language of Celestials. Names are oft derived from the names of celestial bodies, heavenly, grandiose, and carrying much weight. Due to their unearthly forms, names are not typically gendered.",
# namesData=[("Celestial", "Aktia Sial, Dusara, Fyrses, Govias Ma, Ildos, Lynir, Muockthos, Nydis, Phaara Nayin, Ulone, Vophin Sey, Xeytzin, Zeleraka")],nameFormat="{{name}}", traitsDescription="Your Celestial character has the following traits:",
# traitsDescriptions=[("Ability Score Increase", "Your Wisdom score increases by 2, and your Charisma score increases by 1."),
# ("Age", "Celestials are ageless creatures. However, by coming to the physical realm, they make themselves vulnerable; they can be destroyed through war, subjugation, or bloodshed."),("Alignment", "With an eye for the continuation and preservation of fate, Celestials tend toward lawful and/or good."),("Size", "By descending from the Celestial Realm, most Celestials appear similar in build to mortals. Your size is Medium."),("Speed", "Your base walking speed is 30 feet."),("Celestial Knowledge", "You have proficiency in the History and Religion skills."),("Radiant-Born", "As a being created from the stars and heavens, you have immunity to radiant damage."),("Sacrificial Healing", "As a bonus action, you can take from your own health pool to heal a willing creature you can see, so long as doing so will not make you fall unconscious. Roll 1d4, and you can choose to add your Wisdom modifier to the roll. You lose that amount of hit points, but your chosen ally gains them. After using this feature, you cannot use it again until you complete a short or long rest. This dice changes when you reach certain levels. The die becomes 1d6 at 5th level, a 1d8 at 10th level, and a 1d10 at 15th level."),("Sacrificial Shielding", "When a creature you can see takes damage, you can use your reaction to redirect half of the damage to yourself. After using this feature, you cannot use it again until you complete a short or long rest."),("Languages", "You can speak, read, and write Va-Nox and Celestial. The language of Celestials sounds melodic, but it features sounds and grammatical patterns that are incomprehensible to mortal understanding.")],traits=[("Celestial Knowledge", "You have proficiency in the History and Religion skills."),("Radiant-Born", "As a being created from the stars and heavens, you have immunity to radiant damage."),("Sacrificial Healing", "As a bonus action, you can take from your own health pool to heal a willing creature you can see, so long as doing so will not make you fall unconscious. Roll 1d4, and you can choose to add your Wisdom modifier to the roll. You lose that amount of hit points, but your chosen ally gains them. After using this feature, you cannot use it again until you complete a short or long rest. This dice changes when you reach certain levels. The die becomes 1d6 at 5th level, a 1d8 at 10th level, and a 1d10 at 15th level."),("Sacrificial Shielding", "When a creature you can see takes damage, you can use your reaction to redirect half of the damage to yourself. After using this feature, you cannot use it again until you complete a short or long rest.")],stats=[("wisdom", 2), ("charisma", 1)]))

# pyperclip.copy(raceGen(name="Golem",
# flavor="In a land as rich in magic and technology as Runeterra, people have utilized such tools to create constructions. Furthermore, the innate power of the natural world sometimes births sentient constructs, made up of the raw materials from the runic wild. These beings, collectively known as golems, often commit themselves to the service of others. Indeed, the existence of some golems are predicated upon the completion of tasks granted by others. Whether it be undying loyalty to the master who created them, or an exclusive sense of duty to the land from which they emerged, a golem can be counted upon for their unflinching dedication.",
# descriptions=[("Constructions, Categorized", ["The classifications of golems can be specified further. Golems made of machinery and technology, also known as robots, are programmed by the realm's best artificers and technomancers. Other golems can be crafted from more natural substances, like flora and rocks imbued with magic.","While most of these golems have a single master who can be credited with their creation, golems also emerge naturally in the wild. These golems, called sentinels or stone-golems, vary in area of origin and level of sentience. They might be founded from the arcane, living rocks of Ionia to the petrified bark found in Valoran. However, such beings are more comparable to beasts in terms of intelligence."])],nameDescription="As constructions, golems do not follow the same naming conventions as their human counterparts. Inorganic golems are given a name by their creator. Organic golems often derive their names from the materials of which they are created.",namesData=[("Golem", "Beltrite, Cancrite, Duopsion, Incron, Ionase, Kogatz, Mannabar, Marevite, Noremite, Phoelite, Resphur, Sovalt, Surasite, Valile")],nameFormat="{{name}}",traitsDescription="Your golem character has the following traits:", traitsDescriptions=[("Ability Score Increase", "Your Strength score increases by 2."),("Age", "Golems are not born as mortals are, and they do not age as mortals do. They are constructed, so your character's age is based upon when you were created or emerged from the wild."),("Alignment", "Golems, especially inorganic golems, are generally programmed to carry out the will of their creators. Therefore, they tend toward lawful alignments."),("Size", "The most powerful golems—particularly those constructed by legendary artificers or borne of fabled, magical sources—may tower above mortals. However, most appear more human-like in size. Your size is Medium."),("Speed", "Your base walking speed is 30 feet."),("Living Construct", "Even though you were constructed, you are a living creature. You are immune to disease. You do not need to eat, drink, or breathe. Instead of sleeping, you enter an inactive state for 4 hours each day. You do not dream in this state; you are fully aware of your surroundings and notice approaching enemies and other events as normal."),("Natural Armor", "You have an armor bonus of +1 when wearing armor. When you are not wearing armor, your AC is equal to 10 + your natural armor bonus + your dexterity modifier."),("Languages", "You can speak, read, and write Va-Nox."),("Subraces", "Golems can be separated into two subraces, based on their source and materials from which they are made. These categories are inorganic golems and organic golems; choose one such subrace.")],traits=[("Living Construct", "Even though you were constructed, you are a living creature. You are immune to disease. You do not need to eat, drink, or breathe. Instead of sleeping, you enter an inactive state for 4 hours each day. You do not dream in this state; you are fully aware of your surroundings and notice approaching enemies and other events as normal."),("Natural Armor", "You have an armor bonus of +1 when wearing armor. When you are not wearing armor, your AC is equal to 10 + your natural armor bonus + your dexterity modifier.")],stats=[("strength", 2)],subraceDescription="Golems can be separated into two subraces, based on their source and materials from which they are made. These categories are inorganic golems and organic golems; choose one such subrace.",subraces=[
# {
# "name":"Inorganic",
# "desc":"<p>Inorganic golems refer to beings that derive power and energy through man-made means. They are typically made of metal, plating, or other machinery. Such golems might be motorized and made sentient through steam power, electricity, artificing, or even technological magic (called technomancy).</p><p>Inorganic golems are sometimes found throughout Piltover and Zaun, where the blooming culture of invention encourages their construction. Outside of these sister-cities, however, some debate the morality of creating life unnaturally.</p>",
# "traitDescs":[("Ability Score Increase", "Your Intelligence score increases by 1."),
# ("Extra Language", "You are programmed with the ability to imitate another language perfectly. You can speak, read, and write one extra language of your choice."),
# ("Knowledge Programmed", "Your creator designed you with certain competencies. You are proficient in any combination of three skills or tools of your choice."),
# ("Machine's Mastery", '''You are programmed with a practical function or apparatus; choose one trait from the table below.
# <table>
#     <thead>
#         <tr>
#             <td>Trait</td>
#             <td>Description</td>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Climbing Picks</td>
#             <td>You have a climbing speed of 30 feet.  </td>
#         </tr>
#         <tr>
#             <td>Darkvision</td>
#             <td>You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.</td>
#         </tr>
#         <tr>
#             <td>Drills</td>
#             <td>You have a burrowing speed of 30 feet.</td>
#         </tr>
#         <tr>
#             <td>Water Engine</td>
#             <td>You have a swimming speed of 30 feet</td>
#         </tr>
#         <tr>
#             <td>Wheels</td>
#             <td>Your base walking speed increases to 35 feet.</td>
#         </tr>
#     </tbody>
# </table>''')],
# "traits":[("Knowledge Programmed", "Your creator designed you with certain competencies. You are proficient in any combination of three skills or tools of your choice."), ("Machine's Mastery", "DELETE THIS")],
# "stats":[("intelligence", 1), ("strength", 2)]
# },{"name":"Organic",
# "desc":"The pure magic coursing through Runeterra sometimes materializes into elemental or organic golems.",
# "traitDescs":[("Ability Score Increase", "Your Constitution score increases by 1."),
# ("Golem's Muscle", "Your size category is Medium, but you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift."),
# ("Nature's Knowledge", "You are proficient in the Nature skill."),
# ("Natural Weapon", "You are proficient with your unarmed strikes, which deal 1d6 + STR damage on a hit."),
# ("Mask of the Wild", "Your body, constructed of naturally-occuring materials, allows you to easily blend into the environment. You can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls.")],
# "traits":[("Golem's Muscle", "Your size category is Medium, but you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift."),
# ("Nature's Knowledge", "You are proficient in the Nature skill."),
# ("Natural Weapon", "You are proficient with your unarmed strikes, which deal 1d6 + STR damage on a hit."),
# ("Mask of the Wild", "Your body, constructed of naturally-occuring materials, allows you to easily blend into the environment. You can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls.")],
# "stats":[("strength", 2), ("constitution", 1)]}],
# additionalStrings=tableGen("Machine's Mastery", '''<p>You are programmed with a practical function or apparatus; choose one trait from the table below.</p>
# <table>
#     <thead>
#         <tr>
#             <td>Trait</td>
#             <td>Description</td>
#         </tr>
#     </thead>
#     <tbody>
#         <tr>
#             <td>Climbing Picks</td>
#             <td>You have a climbing speed of 30 feet.  </td>
#         </tr>
#         <tr>
#             <td>Darkvision</td>
#             <td>You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.</td>
#         </tr>
#         <tr>
#             <td>Drills</td>
#             <td>You have a burrowing speed of 30 feet.</td>
#         </tr>
#         <tr>
#             <td>Water Engine</td>
#             <td>You have a swimming speed of 30 feet</td>
#         </tr>
#         <tr>
#             <td>Wheels</td>
#             <td>Your base walking speed increases to 35 feet.</td>
#         </tr>
#     </tbody>
# </table>''', [("Climbing Picks","You have a climbing speed of 30 feet."),
# ("Darkvision","You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),
# ("Drills","You have a burrowing speed of 30 feet."),
# ("Water Engine","You have a swimming speed of 30 feet"),
# ("Wheels","Your base walking speed increases to 35 feet.")])))

# pyperclip.copy(raceGen(name="Spirit",flavor="Spirits long precede the existence of human societies and history. Tied intrinsically to realms beyond mortal understanding, spirits are mystical and magical. Spirits draw some sustenance from the mortal world, though that sustenance takes different forms and extents. Demons, for instance, survive on negative aspects of mortal experience, gorging on the resulting manic, charged energy. Meanwhile, Yordles sometimes seek mortal companionship out of natural sociability. In either case, spirits bring supernatural influence to Runeterra.",descriptions=[("Drawn to Emotion",["Some spirits, particularly demons, are born directly from mortal emotion—embodying strong, collective feelings like fear, rage, sorrow, or desire. Others might be summoned by arcanists or cultists, and these spirits may then rely on mortal temptation and ensnarement for survival.","Other spirits, like yordles, may come from their enchanted homeland of Bandle City out of admiration or curiosity regarding the physical world. These more pleasant of these spirits tend to be genial, contributing to human societies and advancements. The more unpleasant of these spirits, however, might be more impish and potentially harmful."]),("Predator and Prey", ["For different reasons, spirits are often considered unwelcome in Runeterra's civilizations. Demons are abhorred as horrid predators, and mythos often emerges about these demonic menaces. As such, these spirits rarely engage in human affairs, instead preferring the cover of night to find isolated victims.", "Yordles, with their unnatural appearance or their less-than-predictable motives, are frequently considered threats to some human societies. Some extremists have taken to hunting yordles without exception. However, some of these spirits have utilized their magic and ingenuity to create glamours. This allows them to appear much more palatable to society and continue interacting with the mortal world."])],nameDescription="The names of spirits do not follow the traditional naming conventions of mortals. Demon names typically stem from what mortals might call them, giving their fears or anxieties identity and physical form. Or, a demon might choose a name from past victims, assuming a different name as time goes on. Contrastingly, yordle names tend to sound friendly and welcoming, with double letters or simple syllabic counts.",namesData=[("Demonic", "Asha, Damethus, Faltas, Redmurne, Yeboros"),("Yordle", "Bicey, Cheelie, Eearey, Fayan, Grari, Jilni, Ledrey, Meevo, Pimmer, Perret, Wultz, Yorro, Zefo")],nameFormat="{{name}}",traitsDescription="Your spirit character has the following traits:",traitsDescriptions=[("Ability Score Increase", "Your Charisma score increases by 2."),("Age", "Spirits age at a much slower rate than humans, and their lifespans are drastically higher, lasting millennia."),("Alignment", "Spirits can be wily and unpredictable; as such, they are rarely of lawful alignments. Demons are often evil in alignment, while yordles tend toward good."),("Size", "Spirit forms vary. If you are a demon, your size is Medium. If you are a yordle, your size is Small."),("Speed", "Your base walking speed is 30 feet."),("Living Spirit", "You are immune to disease. You do not need to eat, but you can ingest food and drink if you wish. Also, instead of sleeping, you enter a sleep-like state. You need to remain in it for only 4 hours each day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."),("Mystical Awareness", "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."),("Spirit Realm's Refuge", "As an action, you can teleport into a pocket of the Spirit Realm. The pocket is about 20 x 20 feet, and you can remain there for one hour. When the hour ends or when you choose, you teleport back to the exact location you were in prior to entering the Spirit Realm, or in the nearest unoccupied space. Once you use this feature, you cannot use it again until you complete three long rests."),("Languages", "You can speak, read, and write Va-Nox and Sylvan, the language of the Spirit Realm."),("Subraces", "Spirits are generally divided into two groups. Demons are malevolent, feasting on the turbulent emotions or desires of mortals. Yordles tend to be more amiable, traversing Runeterra with wellmeant mischief. Choose one of these subraces.")], traits=[("Living Spirit", "You are immune to disease. You do not need to eat, but you can ingest food and drink if you wish. Also, instead of sleeping, you enter a sleep-like state. You need to remain in it for only 4 hours each day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."),("Mystical Awareness", "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."),("Spirit Realm's Refuge", "As an action, you can teleport into a pocket of the Spirit Realm. The pocket is about 20 x 20 feet, and you can remain there for one hour. When the hour ends or when you choose, you teleport back to the exact location you were in prior to entering the Spirit Realm, or in the nearest unoccupied space. Once you use this feature, you cannot use it again until you complete three long rests.")],stats=[("charisma", 2)],subraceDescription="Spirits are generally divided into two groups. Demons are malevolent, feasting on the turbulent emotions or desires of mortals. Yordles tend to be more amiable, traversing Runeterra with wellmeant mischief. Choose one of these subraces.",subraces=[{"name":"Demon","desc":"<p>The appearance of a demon differs wildly. Some accounts claim to have seen a humanoid catfish haunting the gambling halls of Bilgewater. Other legends abound of a lustful demoness who takes whatever form her targets find desirable. Less powerful demons might assume a physical form with which to interact with mortals. Upon the destruction of that form, the spirit returns to the Spirit Realm for recuperation.</p><p>Unholy dwellers of darkness, demons wander the world in search of mortals to make prey. While the intentions demons hold can be hard to pinpoint, they can be assumed to be evil in nature. After all, their specialty might be in consuming and corrupting souls.</p>","traitDescs":[("Ability Score Increase", "Your Wisdom score increases by 1."),("Evil Insight", "Once per long rest, you can look into the weaknesses of a creature you can see. As a bonus action, you can target a creature. Make a Wisdom (Insight) check against that creature's Charisma (Deception). Upon success, you gain advantage on the next attack roll against that creature. Also, you learn the creature's damage vulnerabilities, if any."),("Demonic Darkvision", "Being a demon, you are much accustomed to prowling in the dark. Your darkvision has a radius of 120 feet. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),("Light Aversion", "You are vulnerable to radiant damage.")],"traits":[("Evil Insight", "Once per long rest, you can look into the weaknesses of a creature you can see. As a bonus action, you can target a creature. Make a Wisdom (Insight) check against that creature's Charisma (Deception). Upon success, you gain advantage on the next attack roll against that creature. Also, you learn the creature's damage vulnerabilities, if any."),("Demonic Darkvision", "Being a demon, you are much accustomed to prowling in the dark. Your darkvision has a radius of 120 feet. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),("Light Aversion", "You are vulnerable to radiant damage.")],
# "stats":[("charisma", 2), ("wisdom", 1)]},{"name":"Yordle",
# "desc":"<p>Small and lively, yordles tend to have mammalian features. They have a range of physical characteristics, with male yordles typically appearing more furry while female yordles appearing with smooth, brightly-colored skin.</p><p>Yordles may be one of the most misunderstood beings across Runeterra. Some underestimate them as harmless little creatures without their own ambitions. Others drastically overstate the dangers that yordles pose. Somehow, yordles persist, chasing their aspirations, whether that be making technological advancements in the mortal world or causing ruckus in one's wake.</p>",
# "traitDescs":[("Ability Score Increase", "Your Intelligence score increases by 2."),
# ("Magic Mischief", "Yordles are inherently magical. Once per long rest, you can use your bonus action to do one of the following:<ul><li>Impose advantage on the next spell attack by a willing creature other than yourself.</li><li> Impose disadvantage on the next enemy spell attack.</li><li>Change the damage type of your next successful spell attack.</li></ul>"),("Yordle Ears", "Yordles tend to have large, sometimes fluffy ears. As such, you have advantage on Wisdom (Perception) checks that rely on hearing.")],
# "traits":[("Magic Mischief", "Yordles are inherently magical. Once per long rest, you can use your bonus action to do one of the following:<ul><li>Impose advantage on the next spell attack by a willing creature other than yourself.</li><li> Impose disadvantage on the next enemy spell attack.</li><li>Change the damage type of your next successful spell attack.</li></ul>"),("Yordle Ears", "Yordles tend to have large, sometimes fluffy ears. As such, you have advantage on Wisdom (Perception) checks that rely on hearing.")],
# "stats":[("charisma", 2), ("intelligence", 2)]}]))

pyperclip.copy(raceGen(
name="Vastaya",flavor="Tribes set in the deep wilderness, animalistic features and temperaments, innate connection with Runeterra's magic; the vastayan peoples are unified in these traits. However, the vastaya are diverse and far-reaching, just as the tides of nature itself are chaotic and uncontrollable.",descriptions=[("Blood of the Wild",["The vastaya have differing degrees of animal-like features. Some appear more human-like, with few chimeric traits to distinguish them from their mortal peers. Others are fully animal in appearance. Some even develop combinations of distinct animal characteristics, embodying amalgamations of bestial characteristics in a single body.","Depending on the tribe and connection to ancient magic, vastaya have various levels of shapeshifting ability. Most vastaya maintain a shape that incorporates both animal and humanoid features, with special care for matching the animal ancestry of their tribe (for instance, a vastaya of the reptilian Strig tribe would likely retain their reptilian features.)"]),("Ancient Heritage",["Vastaya trace their lineage to ancient times, particularly to the intermingling of humans and a primeval race called the Vastayashai’rei. As legend states, the Vastayashai’rei originated in the First Lands, which would come to be called Ionia. In a primordial war with titans who rained hell from the skies above, the Vastayashai’rei absorbed the land's natural and spiritual magic into their bodies, becoming vastly powerful.","Thousands upon thousands of years after this war, the vastaya emerged as descendants of these ancient peoples. The vastaya evolved into different brances and tribes, forming their own societies, languages, and civilizations across Runeterra. Now, most vastayan tribes reside in Ionia, a land which still carries inherent magic that gives the life to the vastaya."])],nameDescription="Vastayan names are typically drawn from the vastayan language, but some might be based in Ionian script. Names are given at birth, by parents or by tribe elders, depending on clan traditions.", nameFormat="{{name}}", namesData=[("Male", "Akrato, Brekan, Draclo, Gongram, Ishkan, Marok, Neyerdan, Redalish, Strago, Vilom, Watong"),("Female", "Ahlana, Elmi, Hanni, Irroa, Lakaia, Meian, Neirin, Ohrila, Raini, Sedlani, Sheilah, Viyana, Weeva"),("Gender-Neutral", "Alekhan, Belnani, Halansa, Jerivahn, Mahni, Narene, Rantloa, Songna, Weivam")],traitsDescription="Your Vastaya character has the following traits:",
stats=[("wisdom", 2)], traitsDescriptions=[("Ability Score Increase", "Your Wisdom score increases by 2."),("Age", "Vastaya reach physical maturity at around the same rate as humans, but they stay youthful for longer and have more prolonged lifespans. They can live to be up to 600 years old."),
("Alignment", "Most vastaya care not for the laws of mankind, instead aligning themselves with the chaos of nature and magic. As such, vastaya tend toward chaotic alignments."),
("Size", "Vastaya are comparable in size and weight to humans, ranging between 4 to 6 feet tall, depending on the subrace. Your size is Medium."),("Speed", "Your base walking speed is 30 feet."),
("Innate Shapechanger", "You can cast the second-level spell <em>Alter Self</em>, without expending a spell slot. Once you cast it, you can't do so again until you finish a long rest."),("Knowledge of the Wild", "You are proficient in the Nature and Survival skills."),("Languages", "You can speak, read, and write Va-Nox and Vastayan. The Vastayan language has many dialects originating from the split of different tribes."),("Subraces", "There are numerous branches of vastayan heritage and forms, but they can be generalized into three tribal groupings: Landwalker Tribes, Tribes of the Sea, and Tribes of the Sky. Choose one such subrace.")], traits=[("Innate Shapechanger", "You can cast the second-level spell <em>Alter Self</em>, without expending a spell slot. Once you cast it, you can't do so again until you finish a long rest."),("Knowledge of the Wild", "You are proficient in the Nature and Survival skills."),("Languages", "You can speak, read, and write Va-Nox and Vastayan. The Vastayan language has many dialects originating from the split of different tribes.")],subraceDescription="There are numerous branches of vastayan heritage and forms, but they can be generalized into three tribal groupings: Landwalker Tribes, Tribes of the Sea, and Tribes of the Sky. Choose one such subrace.", subraces=[{"name":"landwalker tribe",
"desc":"<p>As the category suggests, the Landwalker Tribes are made up of vastaya who tread the earth. Generally, Landwalker Tribes are the most numerous and common groups of vastaya found in Runeterra. Landwalker Tribes include branches like the goatlike Fauhwoon, the birdlike Lhotlan, the monkeylike Shimon, and several others.</p>",
"traitDescs":[("Ability Score Increase", "Your Strength score increases by 1."),
("Climbing Speed","You have a climbing speed of 30 feet."),
("Innate Spellcasting", "You know the <em>Druidcraft</em> cantrip."),
("Mask of the Wild", "Used to traversing forests and wilds, you can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls."),
("Speak with Small Beasts", "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts.")],
"traits":[("Innate Spellcasting", "You know the <em>Druidcraft</em> cantrip."), ("Mask of the Wild", "Used to traversing forests and wilds, you can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls."),
("Speak with Small Beasts", "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts.")],
"stats":[("wisdom", 2), ("strength", 1)]},{"name":"Tribe of the Sea",
"desc":"Tribes of the Sea inhabit Runeterra's seas and oceans, able to survive in depths untouched by humans. As a result of living in the oceans, separate from human intervention, they are the most in-touch with Runeterra's natural magic—flowing in its watery depths. They tend to be the least human-like in appearance, needing aquatic traits like gills and fins to thrive in water environments. Tribes of the Sea include the mermen-like Marai, the Makara, and the Raylu.",
"traitDescs":[("Ability Score Increase", "Your Charisma score increases by 1."),
("Amphibious", "You can breathe on land and in water."),
("Innate Spellcasting", "You know the <em>Shape Water</em> cantrip."),
("Swimming Speed", "You have a swimming speed of 30 feet."),
("Sea Weapon Training", "You have proficiency with spears, tridents, and nets.")],
"traits":[("Innate Spellcasting", "You know the <em>Shape Water</em> cantrip."),
("Amphibious", "You can breathe on land and in water."),
("Sea Weapon Training", "You have proficiency with spears, tridents, and nets.")],
"stats":[("wisdom", 2)]}, {"name":"Tribe of the sky",
"desc":"Tribes of the Sky vastaya live far above the lands of humans, in the skies, trees, and mountains. Tribes of the Sky include the Besheb, the Strig, the Chyra, and other unidentified tribes.","traitDescs":[("Ability Score Increase", "Your Dexterity score increases by 1."),
("Innate Spellcasting", "You know the <em>Gust</em> cantrip."),
("Talons", "Your have talons, which can act as natural weapons and be used to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Dexterity modifier, instead of the bludgeoning damage normal for an unarmed strike."),
("Wings", "You have a flying speed of 30 feet. You must be in a space wide enough to accommodate your wingspan to fly. Your wingspan is equal to twice your height. You cannot fly if you are wearing armor you are not proficient in, armor not tailored to accommodate your wings, or a backpack not specially tailored to your wings.")],
"traits":[("Innate Spellcasting", "You know the <em>Gust</em> cantrip."),
("Talons", "Your have talons, which can act as natural weapons and be used to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Dexterity modifier, instead of the bludgeoning damage normal for an unarmed strike."),
("Wings", "You have a flying speed of 30 feet. You must be in a space wide enough to accommodate your wingspan to fly. Your wingspan is equal to twice your height. You cannot fly if you are wearing armor you are not proficient in, armor not tailored to accommodate your wings, or a backpack not specially tailored to your wings.")],
"stats":[("wisdom", 2)]}]))