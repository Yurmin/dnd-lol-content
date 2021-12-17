<!-- markdownlint-disable MD033 -->

# Races

## Ascended

name="Ascended"

flavor="Transformed by an ancient, divine disc or merged with a celestial power, the Ascended are elevated beyond their mortal states into legendary, powerful beings. Physically, they are indelibly evolved, made more powerful, more swift, and more resilient. Their minds are changed as well; indeed, due to their exalted station, they are concerned with matters far above the day-to-day matters of mortals. From protecting the noble tenets of justice and truth to pursuing world-ending revenge, the nature of an individual Ascended depends on their life as a mortal and the nature of their Ascension. No matter the motivation, the presence of an Ascended points to universe-altering events to come."

descrptions=[
("Beyond Mortal Bounds",["Extremely rare, the Ascended are some of the most powerful beings to roam Runeterra. With inhuman speed, strength, and stamina, the Ascended are called to commit themselves to otherworldly, far-reaching causes.","The physical form of such a being shows undeniable evidence of their Ascension. The Shuriman Ascended fuse with the image of an animal, assuming a beastly and noble quality. The Targonian Ascended, though human in likeness, may have characteristics that reveal the celestial that resides within them. For instance, Leona, the Aspect of the Sun, seems to physically shine with the power of the Sun, and her eyes burn with its brightness. The Darkin warp the bodies of their mortal hosts, slowly decaying the form through corrupt energy and blood magic.","Although immune to most natural causes of death, the Ascended can be defeated in some manner. Particular weapons and magics exist that can maim or kill Shuriman and Targonian Ascended, and the Darkin can be sealed within their weapons so long as they are without a host."]

### Shuriman names

nameDescription="As both the Shuriman Ascended and the Darkin reached Ascension during the reign of the Shuriman Empire, their names are based in the Ancient Shuriman language. The Darkin, according to their leader Aatrox, frequently have doubled vowels in their names. The Targonian Ascended tend to keep their mortal, mundane names rather than assume the identity of the celestial aspect within them (see Targonian Humans)."

namesData=[
("Shuriman", "Az'ravi, Bahatek, Esh'kai, Ishtaka, Nacrath, Nixa, Retekta, Sek'riza, Xeyush"), ("Darkin", "Aalrut, Ceheltox, Khaal, Ma'almar, Nek'xast, Rhelaas, Seltaava, Shalteeya, Taltarus, Virresh, Xuust")
]

### Ascended Traits

traitsDescription="Your Ascended character has the following traits:"

traitsDescriptions=[
("Ability Score Increase", "Your Dexterity score increases by 2."),
("Age", "Prior to becoming Ascended, these beings age according to their mortal life. After Ascension, their aging slows and their natural lifespans are drastically increased, spanning millennia."),
("Alignment", "The Ascended are steadfast in their ambitions; without personal appetite and vigor, their Ascension would undoubtedly fail. As such, they are rarely of totally neutral alignments. Targonian Ascended tend toward good alignments, while Darkin tend toward evil."),
("Size", "Some retain their human frame when becoming Ascended, and others are altered in size and shape after the transformation. As such, Ascended vary from about 5 feet to over 7 feet tall. Your size is Medium."),
("Speed", "Your base walking speed is 30 feet."),
("Ascended Endurance", "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest."),
("Languages", "You can speak, read, and write Va-Nox."),
("Subrace", "The different processes of Ascension divides the Ascended into Shuriman Ascended and Targonian Ascended. From there, the Darkin are formerly Shuriman Ascended who have been corrupted through war and betrayal. Choose one of these subraces.")
]

traits=[("Ascended Endurance", "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.")]

#### Shuriman Ascended

{
"name":"Shuriman Ascended",
"desc":,
"traitdescs":,
"traits":,
"stats":

Millennia ago, during the height of the Shuriman Empire, Shuriman warriors of exceptional loyalty and ability had been selected for a rite known as the Ritual of Ascension. Through the power of an ancient, colossal artifact known as the Sun Disc of Shurima, these warriors had been imbued with mystic energy.Based on the ideals they uphold and Shurima's culture of symbolism, they are merged with an aligning animalistic spirit. These beings harbor great physical strength, stature, and resilience. Indeed, when the sun had not yet set on the Empire of Shurima, these beings made up an Ascended legion, the Sunborn, charged with protecting Shurima and Azir.

In the days of the empire's decline, the Ritual of Ascension had failed with greater frequency. Unsuccessful Ascensions either killed those who participated in the ceremony or produced failed, scarred Ascended called Baccai. Furthermore, most of the Ascended of ancient times had been destroyed in battles with the Void and in civil wars. Nonetheless, the recent resurrection of the Shuriman emperor Azir and his following Ascension reveals that the

Sun Disc may yet claim the worthy for its sacred transformation.

**_Ability Score Increase._** Your Constitution score increases by 1.

**_Blessing of the Sun Disc._** <p>The transformation has gifted you with a unique ability based on the studies and nature of your life as a human. Select one from the list below or work with the DM to craft a blessing of similar power:</p>

<table>
    <thead>
        <tr>
            <th>Blessing</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>Ascended Fury</th>
            <td><p>When successfully landing an attack that deals bludgeoning, piercing, or slashing damage, you can channel Ascended Fury to cause that attack to deal another 1d6 + STR damage. After using this blessing, you can't use it again until you complete a long rest.</p><p>This damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 1d12 at 10th level, and a 2d12 at 15th level.</p></td>
        </tr>
        <tr>
            <th>Ghost of the Soldier</th>
            <td><p>As a bonus action, you can conjure a Sand Soldier within 15 feet of you and in an empty space with 5 feet on all sides.
            <ul><li>It can make a melee spear attack for 1d6 + DEX.</li> <li>Your movement can be used to move the soldier.</li><li>The soldier cannot perceive anything.</li><li> The soldier has hit points equal to 1d6 + CHA.</li><li>The soldier dissolves after 1 minute or if you are not within 15 feet of it.</li></ul>After using this blessing, you can't use it again until you complete a long rest. </p> <p>The damage die changes when you reach certain levels. The die becomes 2d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p></td>
        </tr>
        <tr>
            <th>Life Siphon</th>
            <td><p>As an action, roll 1d6 + CHA against a creature you can see. You take this amount of hit points away from the target and add it to your own. The target may make a DC 13 CON saving throw to resist, losing half the amount of hit points on a successful save. This has no effect on Constructs or Undead. After using this blessing, you can't use it again until you complete a long rest.</p> <p>The damage die changes when you reach certain levels. The die becomes 1d10 at 5th level, a 2d12 at 10th level, and a 3d12 at 15th level.</p></td>
        </tr>
    </tbody>
</table>

**_Desert Terrain Familiarity._** When traveling in desert terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.

**_Extra Languages._** You can speak, read, and write in Ancient Shuriman and Modern Shuriman.
}

<!--------------- ASCENDED - TARGONIAN ASCENDED --------------->

#### Targonian Ascended

The peak of Mount Targon exudes celestial power. The apex is the apparent portal between the physical world and Targon Prime, a celestial realm where beings known as Aspects live. But the mountain is nigh impossible to scale. Hidden by a layer of clouds, its rocky paths shift constantly—the land itself altered by a higher magic. Even reaching the top of the mountain is not a guarantee of one's success. Some may find empty ruins at the mountaintop, reflecting their soul's unworthiness. The ascent is the ultimate challenge of one's endurance, skill, dedication, and spirit.

Most mortals lose their lives in the climb. But for the few that make it—and for the fewer that the mountain finds worthy—they are rewarded with heavenly magic. The stellar Aspects, who embody concepts and constellations, may bestow some of their power unto a deserving mortal. Or, the Aspect may even fuse with a mortal, leaving the celestial plane and elevating the mortal into an almighty host.

**_Ability Score Increase._** Your Charisma score increases by 1.

**_Blessing of the Aspect._** Scaling Mount Targon has convinced an Aspect to grant you their power. Consider your bond with this Aspect; have they bestowed you a shred of their abilities? Or have they fully merged with you, erasing your previous identity? Select one from the list or work with the DM to craft a blessing of similar power:

<table>
    <thead>
        <tr>
            <th>Blessing</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Aspect of Destiny</td>
            <td>While out of combat, you may use this blessing to alter the threads of fate. Predict and describe events of the next three in-game minutes. The DM can determine if these events will be Easy (DC 10), Medium (DC 13), Hard (DC 17), or Impossible (DC 20) to occur. Then, roll 1d20. On a successful role, events happen as described. After using this blessing (on a success or fail), you can't use it again until you complete a short or long rest.</td>
        </tr>
        <tr>
            <td>Aspect of Health</td>
            <td>As an action, you may invoke your Aspect to heal yourself or another willing creature you see for 1d6 + CHA. After using this blessing, you can't use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes 1d10 at 5th level, 1d12 at 10th level, and 2d12 at 15th level.</td>
        </tr>
        <tr>
            <td>Aspect of the Messenger</td>
            <td>You can establish a link of telepathic communication between yourself and any creature or entity that you have met before, across any distance. They must be able to comprehend a language you share. The link lasts for 5 minutes. In order to maintain the link, the rules of Concentration apply. After using this blessing, you can't use it again until you complete a long rest.</td>
        </tr>
        <tr>
            <td>Aspect of Revelry</td>
            <td>When prompted to make a Charisma check, you can use this blessing to add +10 to the roll. After using this blessing, you can't use it again until you complete a long rest.</td>
        </tr>
    </tbody>
</table>

**_Extra Language._** You can speak, read, and write in Targonian.

**_Mountainous Terrain Familiarity._** When traveling in mountainous terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.

<!--------------- ASCENDED - DARKIN --------------->

#### Darkin

Once god-warriors in the Ascended legion of the ancient Shuriman Empire, the Darkin are Ascended who have fallen far from grace. Several horrors and betrayals led to their irreversible corruption.

Fighting off the Void from consuming Runeterra exposed them to unspeakable abominations and catastrophic brutality. The fall of the emperor Azir and the collapse of the empire caused infighting in the Ascended legion, leaving many to feel purposeless, adrift. In this conflict between the Ascended, known as the Darkin War, those that would become the Darkin developed blood magic, forming and reforming their bodies. This war raged over Runeterra, with the Darkin taking countless mortal lives to fuel their magic and heal their wounds.

But ultimately, the Darkin were sealed away due to the intervention of the Targonians, particularly the Aspect of Twilight, a Targonian Ascended. The Aspect of Twilight taught mortals the magic necessary to entrap Darkin beings within their own weapons, if not outright destroyed. The Darkin War ended with the Darkin being suppressed and scattered; as centuries passed, the knowledge of their world-ending existence and capabilities fell into obscurity. But in recent times, mortals have found these once-hidden weapons and sought to wield them—potentially reviving these apocalyptic beings. When a mortal picks up a Darkin weapon, they are almost always instantly destroyed, their body overtaken and morphed into the Darkin’s physical host.

**_Ability Score Increase._** Your Strength score increases by 1.

**_Blood Magic._** The Darkin created and perfected the arcane power of blood magic, called hemomancy. As a bonus action, you can use this knowledge to heal your wounds for 1d6 + CHA hit points. After you use this feature, you can’t use it again until you complete a long rest. The dice changes when you reach certain levels. The die becomes a d10 at 5th level, a d12 at 10th level, and a d20 at 15th level.

**_Sealed Weapon._** All existing Darkin are inseparably tied to their weapon of choice. You are proficient in this weapon. In order to roam the world, the Darkin requires a mortal to take hold of the weapon and become their host. In doing so, the host's mind and identity are erased, and their body becomes possessed by the Darkin. The weapon must remain within 10 feet of the Darkin at all times. Without a host, the Darkin’s consciousness is plunged in darkness, without the ability to see or feel until another mortal attempts to wield them.

**_Vengeance of the Darkin._** The Darkin have an appetite for bloodshed; using your sealed weapon, you can critically hit on a 19 or 20. When you critically hit with the sealed weapon, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.

**_Extra Languages._** You can speak, read, and write in Ancient Shuriman and the native language of your mortal host.

<!-- CELESTIAL -->

## Celestial

name="Celestial",
flavor="Old as the universe and just as powerful, Celestials cross the boundaries of mortal possibility. With vast ranges of abilities, such as the power of creation, healing, or omniscience, Celestials demonstrate great providence over the physical realm. However, most Celestials are inhuman, bordering on eldritch in appearance, utterly disconnected from the mortals they ostensibly oversee. While most Celestials choose to remain in the Celestial Realm, content in their incomprehensibility, a select few decide to descend into the mortal realm. But these Celestials almost never come in their pure, godlike forms. Instead, they typically sacrifice some condition of their sublimity in order to better interact with mortals. Or, they may even imbue their essence within mortals, merging with someone worthy and willing.",
descriptions=[("Hands of Fate", ["Celestials are the weavers of destiny, with the power to guide fate toward its course. From the domain of the Celestial Realm, fully-powered Celestials exercise the breadth of their influence. Celestials, knowledgable in the different threads of fate, aim their efforts in preserving the multiverse's longevity. This might be interpreted as goodness or benevolence, but it is perhaps more accurate to acknowledge Celestial actions as being beyond mortal grasp. Indeed, some Celestials pursue more ambivalent strands and developments, such as creating change for change's sake."]),
("Aspects and Visionaries",["A specific type of Celestial exists, residing and originating in a plane called Targon Prime, known as Aspects. The Aspects personify a concept, such as war, justice, or change. These concepts evolve through mortal affairs. At times that necessitate widespread transformation, or if a mortal proves themselves worthy in the ritual of Ascension, an Aspect comes down and merges with a mortal. In this form, an Aspect can be destroyed by a being of equal power, or the Aspect may choose a different mortal host."]),("Humanity's Guardians", ["Some mortal faiths are based in the worship of Celestials. But most followers have not born witness to an actual Celestial, nor have they seen their direct influence. Nonetheless, Celestials may take a hands-on or hands-off approach to helping humans. Stories around Mount Targon spread of a Celestial who sacrificed her immortal, animalistic form and exchanged it for corporeality—embracing all the weaknesses of humanity to better serve them. For all the cruelty of mortals, it seems there are entities dedicated to saving them."]),("Stellar Influence", ["Celestial agency takes different forms. The mythos of the creation of the Ascended claims that Celestials made them as weapons against the Void's corruption. Another type of Celestial exists, called Celestial dragons. These beings manipulate the stars and suns themselves. These dragons may explain the existence of celestial bodies and universes as creations by a higher being.
In either case, Celestial power seems tied to the stars, and thus Celestials have appointed themselves as the guardians of all that the stars cover."])],
nameDescription="Celestial names are based in the language of Celestials. Names are oft derived from the names of celestial bodies, heavenly, grandiose, and carrying much weight. Due to their unearthly forms, names are not typically gendered.",
namesData=[("Celestial", "Aktia Sial, Dusara, Fyrses, Govias Ma, Ildos, Lynir, Muockthos, Nydis, Phaara Nayin, Ulone, Vophin Sey, Xeytzin, Zeleraka")],nameFormat="{{name}}",traitsDescription"Your Celestial character has the following traits:",
traitsDescriptions=[("Ability Score Increase", "Your Wisdom score increases by 2, and your Charisma score increases by 1."),
("Age", "Celestials are ageless creatures. However, by coming to the physical realm, they make themselves vulnerable; they can be destroyed through war, subjugation, or bloodshed."),("Alignment", "With an eye for the continuation and preservation of fate, Celestials tend toward lawful and/or good."),("Size", "By descending from the Celestial Realm, most Celestials appear similar in build to mortals. Your size is Medium."),("Speed", "Your base walking speed is 30 feet."),("Celestial Knowledge", "You have proficiency in the History and Religion skills."),("Radiant-Born", "As a being created from the stars and heavens, you have immunity to radiant damage."),("Sacrificial Healing", "As a bonus action, you can take from your own health pool to heal a willing creature you can see, so long as doing so will not make you fall unconscious. Roll 1d4, and you can choose to add your Wisdom modifier to the roll. You lose that amount of hit points, but your chosen ally gains them. After using this feature, you cannot use it again until you complete a short or long rest. This dice changes when you reach certain levels. The die becomes 1d6 at 5th level, a 1d8 at 10th level, and a 1d10 at 15th level."),("Sacrificial Shielding", "When a creature you can see takes damage, you can use your reaction to redirect half of the damage to yourself. After using this feature, you cannot use it again until you complete a short or long rest."),("Languages", "You can speak, read, and write Va-Nox and Celestial. The language of Celestials sounds melodic, but it features sounds and grammatical patterns that are incomprehensible to mortal understanding.")],traits=[("Celestial Knowledge", "You have proficiency in the History and Religion skills."),("Radiant-Born", "As a being created from the stars and heavens, you have immunity to radiant damage."),("Sacrificial Healing", "As a bonus action, you can take from your own health pool to heal a willing creature you can see, so long as doing so will not make you fall unconscious. Roll 1d4, and you can choose to add your Wisdom modifier to the roll. You lose that amount of hit points, but your chosen ally gains them. After using this feature, you cannot use it again until you complete a short or long rest. This dice changes when you reach certain levels. The die becomes 1d6 at 5th level, a 1d8 at 10th level, and a 1d10 at 15th level."),("Sacrificial Shielding", "When a creature you can see takes damage, you can use your reaction to redirect half of the damage to yourself. After using this feature, you cannot use it again until you complete a short or long rest.")],stats=[("wisdom", 2), ("charisma", 1)]

<!--------------- GOLEM --------------->

## Golem

name="Golem",
flavor="In a land as rich in magic and technology as Runeterra, people have utilized such tools to create constructions. Furthermore, the innate power of the natural world sometimes births sentient constructs, made up of the raw materials from the runic wild. These beings, collectively known as golems, often commit themselves to the service of others. Indeed, the existence of some golems are predicated upon the completion of tasks granted by others. Whether it be undying loyalty to the master who created them, or an exclusive sense of duty to the land from which they emerged, a golem can be counted upon for their unflinching dedication.",
descriptions=[("Constructions, Categorized", ["The classifications of golems can be specified further. Golems made of machinery and technology, also known as robots, are programmed by the realm's best artificers and technomancers. Other golems can be crafted from more natural substances, like flora and rocks imbued with magic.","While most of these golems have a single master who can be credited with their creation, golems also emerge naturally in the wild. These golems, called sentinels or stone-golems, vary in area of origin and level of sentience. They might be founded from the arcane, living rocks of Ionia to the petrified bark found in Valoran. However, such beings are more comparable to beasts in terms of intelligence."])],nameDescription="As constructions, golems do not follow the same naming conventions as their human counterparts. Inorganic golems are given a name by their creator. Organic golems often derive their names from the materials of which they are created.",namesData=[("Golem", "Beltrite, Cancrite, Duopsion, Incron, Ionase, Kogatz, Mannabar, Marevite, Noremite, Phoelite, Resphur, Sovalt, Surasite, Valile")],nameFormat="{{name}}",traitsDescription="Your golem character has the following traits:", traitsDescriptions=[("Ability Score Increase", "Your Strength score increases by 2."),("Age", "Golems are not born as mortals are, and they do not age as mortals do. They are constructed, so your character's age is based upon when you were created or emerged from the wild."),("Alignment", "Golems, especially inorganic golems, are generally programmed to carry out the will of their creators. Therefore, they tend toward lawful alignments."),("Size", "The most powerful golems—particularly those constructed by legendary artificers or borne of fabled, magical sources—may tower above mortals. However, most appear more human-like in size. Your size is Medium."),("Speed", "Your base walking speed is 30 feet."),("Living Construct", "Even though you were constructed, you are a living creature. You are immune to disease. You do not need to eat, drink, or breathe. Instead of sleeping, you enter an inactive state for 4 hours each day. You do not dream in this state; you are fully aware of your surroundings and notice approaching enemies and other events as normal."),("Natural Armor", "You have an armor bonus of +1 when wearing armor. When you are not wearing armor, your AC is equal to 10 + your natural armor bonus + your dexterity modifier."),("Languages", "You can speak, read, and write Va-Nox."),("Subraces", "Golems can be separated into two subraces, based on their source and materials from which they are made. These categories are inorganic golems and organic golems; choose one such subrace.")],traits=[("Living Construct", "Even though you were constructed, you are a living creature. You are immune to disease. You do not need to eat, drink, or breathe. Instead of sleeping, you enter an inactive state for 4 hours each day. You do not dream in this state; you are fully aware of your surroundings and notice approaching enemies and other events as normal."),("Natural Armor", "You have an armor bonus of +1 when wearing armor. When you are not wearing armor, your AC is equal to 10 + your natural armor bonus + your dexterity modifier.")],stats=[("strength", 2)],subraceDescription="Golems can be separated into two subraces, based on their source and materials from which they are made. These categories are inorganic golems and organic golems; choose one such subrace.",subraces=[
{
"name":"Inorganic",
"desc":"<p>Inorganic golems refer to beings that derive power and energy through man-made means. They are typically made of metal, plating, or other machinery. Such golems might be motorized and made sentient through steam power, electricity, artificing, or even technological magic (called technomancy).</p><p>Inorganic golems are sometimes found throughout Piltover and Zaun, where the blooming culture of invention encourages their construction. Outside of these sister-cities, however, some debate the morality of creating life unnaturally.</p>",
"traitDescs":[("Ability Score Increase", "Your Intelligence score increases by 1."),
("Extra Language", "You are programmed with the ability to imitate another language perfectly. You can speak, read, and write one extra language of your choice."),
("Knowledge Programmed", "Your creator designed you with certain competencies. You are proficient in any combination of three skills or tools of your choice."),
("Machine's Mastery", '''You are programmed with a practical function or apparatus; choose one trait from the table below.
<table>
    <thead>
        <tr>
            <td>Trait</td>
            <td>Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Climbing Picks</td>
            <td>You have a climbing speed of 30 feet.  </td>
        </tr>
        <tr>
            <td>Darkvision</td>
            <td>You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.</td>
        </tr>
        <tr>
            <td>Drills</td>
            <td>You have a burrowing speed of 30 feet.</td>
        </tr>
        <tr>
            <td>Water Engine</td>
            <td>You have a swimming speed of 30 feet</td>
        </tr>
        <tr>
            <td>Wheels</td>
            <td>Your base walking speed increases to 35 feet.</td>
        </tr>
    </tbody>
</table>''')],
"traits":[("Knowledge Programmed", "Your creator designed you with certain competencies. You are proficient in any combination of three skills or tools of your choice."), ("Machine's Mastery", "DELETE THIS")],
"stats":[("intelligence", 1), ("strength", 2)]
},{"name":"Organic",
"desc":"The pure magic coursing through Runeterra sometimes materializes into elemental or organic golems.",
"traitDescs":[("Ability Score Increase", "Your Constitution score increases by 1."),
("Golem's Muscle", "Your size category is Medium, but you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift."),
("Nature's Knowledge", "You are proficient in the Nature skill."),
("Natural Weapon", "You are proficient with your unarmed strikes, which deal 1d6 + STR damage on a hit."),
("Mask of the Wild", "Your body, constructed of naturally-occuring materials, allows you to easily blend into the environment. You can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls.")],
"traits":[("Golem's Muscle", "Your size category is Medium, but you count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift."),
("Nature's Knowledge", "You are proficient in the Nature skill."),
("Natural Weapon", "You are proficient with your unarmed strikes, which deal 1d6 + STR damage on a hit."),
("Mask of the Wild", "Your body, constructed of naturally-occuring materials, allows you to easily blend into the environment. You can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls.")],
"stats":[("strength", 2), ("constitution", 1)]}],
additionalStrings=tableGen("Machine's Mastery", '''<p>You are programmed with a practical function or apparatus; choose one trait from the table below.</p>
<table>
    <thead>
        <tr>
            <td>Trait</td>
            <td>Description</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Climbing Picks</td>
            <td>You have a climbing speed of 30 feet.  </td>
        </tr>
        <tr>
            <td>Darkvision</td>
            <td>You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.</td>
        </tr>
        <tr>
            <td>Drills</td>
            <td>You have a burrowing speed of 30 feet.</td>
        </tr>
        <tr>
            <td>Water Engine</td>
            <td>You have a swimming speed of 30 feet</td>
        </tr>
        <tr>
            <td>Wheels</td>
            <td>Your base walking speed increases to 35 feet.</td>
        </tr>
    </tbody>
</table>''', [("Climbing Picks","You have a climbing speed of 30 feet."),
("Darkvision","You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),
("Drills","You have a burrowing speed of 30 feet."),
("Water Engine","You have a swimming speed of 30 feet"),
("Wheels","Your base walking speed increases to 35 feet.")])

<!-- HUMAN -->

## Human

name="Human",
flavor="Coming from nearly all major lands and inhabiting all walks of life, humans are the most common peoples of Runeterra. All humans are thought to have originated from either the First Lands—which would later be known as Ionia—or the Freljord, thousands and thousands of years ago. Humans have therefore shaped millennia of ancient and contemporary history. Through countless generations of migration, warfare, unity, regression, progress, and other seeming contradictions, humans have created institutions and civilizations that define life on Runeterra.", traitsDescription="Your human character has the following traits:", traitsDescriptions=[
    ("Ability Score Increase", "Two different ability scores of your choice increase by 1."),
    ("Age", "The markers of adulthood vary by the cultures of Runeterra, but it is generally agreed that humans are adults by their late teen years. They typically live up to a century."),
    ("Alignment", "Humans vary in personality and loyalty. As such, they lack a tendency toward any particular alignment."),
    ("Size", "Humans differ in build and physique, generally ranging from 4 feet to 7 feet tall. Your size is Medium."),
    ("Speed", "Your base walking speed is 30 feet."),
    ("Languages", "You can speak, read, and write Va-Nox and the language of your region (see Chapter 3: Locations and Languages"),
    ("Subraces", "The humans of Runeterra can be assorted by regional lines. Each region grants a character different traits. See below and choose one such region from which you hail. Or, the Dungeon Master might work with you to combine regions and traits, creating dual heritage."),
], subraceDescription="The humans of Runeterra can be assorted by regional lines. Each region grants a character different traits. See below and choose one such region from which you hail. Or, the Dungeon Master might work with you to combine regions and traits, creating dual heritage.",

### Human subraces

#### Bilgewater

In the southeastern reaches of Runeterra lie the Serpent Isles, encompassing the port city of Bilgewater and indigenous island cultures. The Bilgewater area is notorious for its lawlessness, piracy, gambling, and trading. The chaos of Bilgewater often leads its people to seek fame and fortune—but they must be prepared to brave the deadly waters and even deadlier rivals.

**_Ability Score Increase._** Your Dexterity score increases by 1.

**_Extra Feat._** You have the Tavern Brawler feat.

**_Vehicle Proficiency._** You have proficiency with water vehicles.

**Bilgewater Names:** (Male) Dover, Dunstan, Glade, Harlan, Jackwin; (female) Bellamy, Henrietta, Maye, Nanie, Raven;
(gender-neutral) Artie, Brooks, Cyd, Rossa, Roxa; (surnames) Drachen, Godwin, Hawkins, Hammond, Lynley

**Buhru/Indigenous Serpent Isle Names:** (Male) Amakoa, Halloa, Hekilli, Keoi, Okao; (female) Illhia, Kalia, Kaioni, Makama, Meitu; (gender-neutral) Ioelu, Laotl, Luhklu, Noelu, Waiolal; (surnames) Allani, Eilikapao, Iakouros, Kapele, Mei Mele

#### Demacia

Located in the west side of the continent Valoran, the mighty kingdom of Demacia prides itself on its dedication to justice. That sense of justice, however, is often defined in direct opposition to mages and sorcery. The monarchy of Demacia might call upon its citizens to act in service to and defense of its decorated military history.

**_Ability Score Increase._** Your Strength score increases by 1.

**_Demacian Bravery._** You have advantage on saving throws against being frightened.

**_Extra Feat._** You have the Mage Slayer feat.

**Demacian Names:** (Male) Erhard, Filivere, Merten, Orlon, Percivale, Terrin; (female) Agathe, Allena, Emaura, Madlyn,Nariella, Sarra; (gender-neutral) Arwynn, Evra, Heike, Jacklin, Jesmin, Rylin; (surnames) People of common birth generally do not have last names, and they instead distinguish themselves by using the name of their hometown (ex: Quinn of Uwendale). However, nobles do have surnames, examples of which include: Hadwise, Hellissent, Roseaman, Salbourne, Vendereye, Winefred

#### Freljord

The Freljord, the relentless tundra of the north, is home to tribes of warriors, marauders, and survivors. Despite the fact that its people are divided into numerous war bands and sects, the frozen expanse cultivates a universal culture of resilience and endurance. Furthermore, a rich mythology of primeval gods and elemental worship spreads through the Freljord’s traditions. However, a civil war brews and braces among three primary factions of the Freljord, prompting Freljordians to venture from the security of their home clan.

**_Ability Score Increase._** Your Constitution score increases by 1.

**_Arctic Terrain Familiarity._** When traveling in arctic terrain, you gain advantage on the following skill checks, related to navigating, traversing, or examining the terrain: Intelligence (Investigation, Nature); Wisdom (Perception, Survival).

**_Extra Feat._** You have the Savage Attacker feat.

##### Variant Trait: Heritage of the Freljord

Though exceedingly rare, some Freljordians are born with magic in their blood. Depending on the type of heritage, this bloodline allows them to manipulate one of the following elements: fire, ice, or storm. Your Dungeon Master might allow you to take up this variant trait. Doing so would replace the Freljord human’s Extra Feat trait. Choose one type of heritage, listed on the next page.

<table>
    <thead>
        <tr>
            <th>Heritage</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Fireborn</td>
            <td>Thought to be near-extinct after the fall of the forge god Ornn and his followers, the Hearthblood. You know the Produce Flame cantrip. Charisma is your spellcasting modifier for that spell.</td>
        </tr>
        <tr>
            <td>Iceborn</td>
            <td>As a human who can touch and manipulate True Ice, you know the Ray of Frost cantrip. Charisma is your spellcasting modifier for that spell.</td>
        </tr>
        <tr>
            <td>Storm-born</td>
            <td>The Stormborn hail from the Ursine clan, which boasts human shapeshifters. They also follow the storm deity Volibear. You know the Shocking Grasp cantrip. Charisma is your spellcasting modifier for that spell.</td>
        </tr>
    </tbody>
</table>

**Freljordian Names:** (Male) Dwenmïr, Hekstrum, Jurhle, Roluf, Skavolf, Stauv; (female) Esju, Irhild, Maikenna, Sylda, Vivrunn, Yannette; (gender-neutral) Katele, Kerdyl, Magne, Rukeve, Synne; (surnames) Rather than surnames, Freljordians tend to take up the name of their clan to mark their background [ex: Ashe of the tribe Avarosa].

#### Ionia

An archipelago on the eastern side of Runeterra, Ionia is best known for its harmony with nature, magic, and spirituality. But beneath this ostensible tranquility, burgeoning among Ionia’s picturesque forests, is darkness. Displaced by Noxian invasion and wartime infighting, several groups and factions have emerged—each with their own vision for the future of Ionia.

**_Ability Score Increase._** Your Wisdom score increases by 1.

**_Extra Feat._** You have the Sentinel feat. SENTINEL (Source: 5e Basic Rules)

You have mastered techniques to take advantage of every drop in any enemy’s guard, gaining the following benefits: • When you hit a creature with an opportunity attack, the creature’s speed becomes 0 for the rest of the turn.• Creatures within 5 feet of you provoke opportunity attacks from you even if they take the Disengage action before leaving your reach.• When a creature within 5 feet of you makes an attack against a target other than you (and that target doesn’t have this feat), you can use your reaction to make a melee weapon attack against the attacking creature.

**_Ionian Weapon Proficiency._** You are proficient in one simple weapon and one martial weapon from the following list. Choose these weapons from the table below.

##### Ionian Weapons

|   Name    |   Cost   | Damage       | Weight  | Properties                                    |
| :-------: | :------: | :----------- | :------ | :-------------------------------------------- |
| _Simple_  | _Melee_  | _Weapons_    |         |
|   Kama    |   1gp    | 1d6 slashing | 2 lb.   | Light                                         |
|   Kunai   |   1sp    | 1d4 piercing | 1 lb.   | Finesse, light, thrown (range 20/60)          |
| _Simple_  | _Ranged_ | _Weapons_    |         |
| Shuriken  |   5cp    | 1d4 piercing | 1/2 lb. | Finesse, thrown (range 20/60)                 |
|  Chakram  |   1sp    | 1d4 slashing | 1/2 lb. | Finesse, thrown (range 20/60)                 |
| _Martial_ | _Melee_  | _Weapons_    |         |
|    Dao    |   10gp   | 1d6 slashing | 2 lb.   | Finesse                                       |
|   Jian    |   15gp   | 1d8 slashing | 2 lb.   | Versatile (1d10)                              |
| _Martial_ | _Ranged_ | _Weapons_    |         |
|  Daikyu   |   30gp   | 1d8 piercing | 2 lb.   | Ammunition (range 150/600), heavy, two-handed |

**Ionian Names:** (Male) Akoz, Fong, Maien, Rasmar, Sinan, Wakiya, Yamu; (female) Ashyi, Cai, Chisa, Haruno, Rika, Sunja; (gender-neutral) Ilkiri, Nava, Rojung, Seong, Sumio, Zhenya; (surnames) [In some Ionian cultures, the surname is presented before the given name.] Huifeng, Jian, Keihao, Tsongma, Wanthi, Xia, Yimuna

#### Ixtal

Hidden within the deep jungles and sprawling wilds is the land of Ixtal. East of Shurima, Ixtal stayed hidden for millennia, observing the happenings on Runeterra and choosing to stay isolated. Instead, Ixtali civilization, technology, and social hierarchy has developed in accord with the area’s potent elemental magic.

**_Ability Score Increase._** Your Charisma score increases by 1.

**_Extra Feat._** You have the Elemental Strike feat.
ELEMENTAL STRIKE (Source: Homebrew by [LeonidasTDD](https://www.dndbeyond.com/feats/107071-elemental-strike "Homebrew on DnDBeyond"))

**_Jungle Terrain Familiarity._** When traveling in jungle terrain, you gain advantage on the following skill checks, related to navigating, traversing, or examining the terrain: Intelligence (Investigation, Nature); Wisdom (Perception, Survival).

**_Swamp Terrain Familiarity._** When traveling in swamp terrain, you gain advantage on the following skill checks, related to navigating, traversing, or examining the terrain: Intelligence (Investigation, Nature); Wisdom (Perception, Survival).

#### Noxus

A military powerhouse, the empire of Noxus is a proud, mighty entity. With a grand history of conquest and domination, Noxus has made its mark on Runeterra through warmongering and invasion. Within the Noxian empire itself, the political landscape is ripe with intrigue and conspiracy. However, their civilization is a staunch meritocracy—allowing anyone of any creed to rise through its ranks.

**_Ability Score Increase._** Your Strength score increases by 1.

**_Extra Feat._** You have the Battle Tactician feat.
BATTLE TACTICIAN (Source: My Homebrew)

You are smart and savvy in the art of war, gaining the following benefits:• You gain a +5 bonus to initiative. • At the start of an encounter, you can choose to do one of the following:

--Swap your own initiative roll with one hostile creature.

--Swap the initiative rolls of two of your allies.

**_Noxian Force._** You are proficient in Intimidation and Persuasion.

**Noxian Names:** (Male) Amdry, Dyrron, Falmis, Jonik, Markhann, Syrhos; Velvohr, (female) Adahva, Corrina, Liselotte, Marreike, Ravona, Sorathea, Sylvha; (gender-neutral) Elinn, Heikhe, Ikhe, Katrin, Lutzin, Marrin, Valevin; (surnames) Brackstom, Clasven, Leverenz, Salazehr, Seirend, Tessrich, Weivand

#### Piltover & Zaun

The sister city-states of Piltover and Zaun are known as preeminent places of progress. The nature of progress can be juxtapositional: both forward-thinking and potentially dangerous. Such contrast, of course, applies to Piltover and Zaun. Surrounded by invention and urban advancement, Piltovans and Zaunites often seek improvement of both themselves and the world they inhabit.

**_Ability Score Increase._** Your Intelligence score increases by 1.

**_Extra Feat._** You gain your choice of one of the following feats: Linguist, Skilled, or Observant.

**_Inventor's Gadgets._** Your are proficient with Tinker's Tools and your choice of another set of artisan's tools. Choose one from this list: Alchemist’s Supplies, Brewer’s Supplies, Calligrapher's Supplies, Carpenter's Tools, Cartographer's Tools, Cobbler’s Tools, Cook’s Utensils, Glassblower’s Tools, Jeweler’s Tools, Leatherworker’s Tools, Mason’s Tools, Painter’s Supplies, Potter’s Tools, Smith’s Tools, Weaver’s Tools, Woodcarver’s Tools

**Piltovan & Zaunite Names:** (Male) Callum, Jamarion, Jett, Kason, Kierin, Lukkas, Mastian; (female) Aubria, Bellamine, Carissa, Laranine, Midenna, Olyvia, Thalia; (gender-neutral) Blair, Brynn, Haiden, Danni, Jona, Maddox, Saller; (surnames) Barrera, Burris, Haridson, McLaudris, Reedman, Santian, Searrs

#### Shuriman

In generations past, Shurima was a sprawling empire—a land of golden palaces and prosperity. But millennia have gone by since the empire's fall, and now Shurima consists of numerous cities spread throughout the desert. Within these assorted cities, diverse in culture and custom, trade and artisanship thrive. But move beyond the ports and cities, and the Shuriman desert holds endless, trecherous plains. But the badlands teem with evidence of a bygone empire, calling to explorers and mercenaries alike, who may find rumors of the great Shurima rising once more.

**_Ability Score Increase._** Your Dexterity score increases by 1.

**_Desert Terrain Familiarity._** When traveling in desert terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.

**_Extra Feat._** You have the Dungeon Delver feat.DUNGEON DELVER (Source: 5e Basic Rules)

Alert to the hidden traps and secret doors found in many dungeons, you gain the following benefits: • You have advantage on Wisdom (Perception) and Intelligence (Investigation) checks made to detect the
presence of secret doors. • You have advantage on saving throws made to avoid or resist traps. • You have resistance to the damage dealt by traps. • You can search for traps while traveling at a normal pace, instead of only at a slow pace.

**Shuriman Names:** (Male) Anotu, Dagan'kai, Enlikan, Hadad'ya, Marduun, Shalumin, Su'nye; (female) Emesya, Ishtel, Liliyah, Nuhaya, Su'ha, Tiamtu, Vil'ava; (gender-neutral) An'zet, Il'hu, Melzari, Menkara, Ouza, Sentet, Tanizir; (surnames) Aluvar, Chatahmu, Merapis, Nempetsu, Ran-kheper, Salhair, Ves-khemet

#### Targon

Surrounding the awe-inspiring Mount Targon exist several tribes, who center their survival and faith around the mountain and the area's boundless celestial lights. The largest of these tribes is known as the Rakkor. The mountainous ranges are harsh and sharp, requiring great tenacity from its people.

In order to endure and revere the sacredness of Mount Targon, tribes tend to be deeply religious. Indeed, Targonian society focuses on theocratic hierarchies. The prevailing faith of Targon is the Solari, a group that worships the holy light of the sun. But their mirroring sect, the Lunari, worships the power of the moon, hidden in darkness.

No matter the faith, however, warriors, acolytes, and magicians of Targon often look to protect their clan or the mountain.

**_Ability Score Increase._** Your Constitution score increases by 1.

**_Celestial Faith._** The people of Targon are intensely faithful or spiritual. Your character is either a Solari or Lunari worshiper; choose one and gain the faith's traits from the table.

| Faith  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| :----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Solari | **_Extra Feat._** You have the Sunstrike feat. SUNSTRIKE (Source: My Homebrew) **_Sunlight Protection._** You gain resistance against necrotic damage and radiant damage.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Lunari | **_Extra Feat._** You have the Skulker feat. SKULKER (Source: 5e Basic Rules) You are expert at slinking through shadows. You gain the following benefits: • You can try to hide when you are lightly obscured from the creature from which you are hiding. • When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position. • Dim light doesn’t im pose disadvantage on your Wisdom (Perception) checks relying on sight. **_Lunari Darkvision._** You have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray. |

**_Mountainous Terrain Familiarity._** When traveling in mountainous terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.

**Targonian Names:** (Male) Ermis, Iamdros, Ignatios, Korolos, Matthaios, Paneles, Vasilaes; (female) Alkessia, Edvoxia, Iphgene, Natasa, Phrodanna, Sotiria, Yanna; (gender-neutral) Aleke, Athanas, Leteris, Serafeim, Spiro, Valenti, Zissa; (surnames) Balleli, Cosmea, Euterou, Remerea, Sarkas, Tantalis, Xenelles

#### Void-Altered

The Void, a dimension of unfathomable horrors and depths of nothingness, bleeds into the realm of Runeterra. Thousands of years ago, warfare brought the dreaded abominations of the Void to the surface, maddening or decimating most who had witnessed it. Over time and continued survival efforts, the Void has been mostly suppressed and stamped out from the physical realm. However, Void rifts still exist in uninhabited pockets, such as in the desert barrens of Shurima, the frozen wastelands of the Freljord, or in the suffocating pitches of Runeterra's oceans.

Most humans who find fissures of the Void are driven to insanity—the fragile, mortal mind immediately succumbing to unspeakable terrors. Or, their bodies are near-instantly destroyed, taken by the Void's tendrils and all-consuming abyss. But for the rare, exceptional few, an encounter with the Void brings not destruction, but creation. Instead, the Void might bring unimaginable power, whether that be uncanny knowledge or otherworldly perseverence.

**_Ability Score Increase._** Your Wisdom score increases by 1.

**_Void Black Magic._** Your exposure to the Void has imbued you with necrotic magic. You know the _Sapping Sting_ cantrip. When you reach 3rd level, you know the _Toll the Dead_ cantrip. When you reach 5th level, you can cast the _Arms of Hadar_ spell once per day. This spell does not take up spell slots. Wisdom is your spellcasting ability for these spells.

**Void-Altered Names:** The Void does not birth humans; any humans who are changed by the Void hail from elsewhere. They most commonly come from Shurima, since most rifts to the Void are found there. Consider where your character comes from and choose a name from that region.

<!--------------- MINOTAUR --------------->

## Minotaur

In the wilderness neighboring human civilizations, one might hear the terrifying roar of a minotaur. Especially in the caverns of Noxus or the petrified forests of Demacia, minotaur clans make their claim. Some often dismiss minotaurs as mindless creatures—but it is a fool's flaw to write them off as such. These beings, particularly adept at the art of combat, are very much concerned with the protection of their homelands and their own.

### Bovine Beings

At first glance, some humans mistake minotaurs for the horrors of nightmares. Standing heads tall above humans, with massive horns and bodies covered in fur, minotaurs appear as humanoid bovines. With animalistic features, they are sometimes mistaken for vastaya or Shuriman Ascended, but it is important to note that there is no such relation.

Moreover, minotaurs boast much more intelligence and sentience than their ox or cow counterparts. While their societies are largely secretive and exclusive, they are nonetheless complex and self-reliant.

### Dignity and Strength

Across Runeterra, minotaur clans uphold the order and unity of their tribes. Minotaurs maintain a simple social hierarchy within their societies. The strongest warriors, conquerors, or protectors are often looked to as leaders. But minotaurs stand by a strong sense of honor and communal strength. The weakest of them are not ostracized, but safeguarded and cared for.

Indeed, at the core of minotaur survival are the values of kinship and self-sufficiency. Minotaur clans in a particular region are often interconnected by accords and agreements. With these arrangements for trade and exchange, minotaur tribes rely on each other instead of seeking assistance from other mortal races.

### A Fraught History

Historically, minotaurs have a dark history with other mortals. For their intimidating stature and isolated lives, minotaurs are often seen as perpetual outsiders. Some humans go so far as to call minotaurs monsters, nothing more than senseless animals. This is a perception to which many minotaurs take offense. However, most do not find the worth in attempting to change such misconceptions, instead preferring to stay in the withdrawn safety among kinsen.

Yet in recent times, many minotaur clans have been conscripted to join national armies, particularly those of Demacia or Noxus. In warlike Noxus, however, those who opposed Noxian invasion were enslaved and made to fight in gladiator pits for entertainment. Such minotaurs are exploited for their brutality. As a result, many minotaurs around the Noxus area distrust mortals, and they actively resist the Noxian regime.

### Haughty and Headstrong

Minotaurs can be rugged around the edges due to lives led largely in autonomy. As such, they face others with a healthy amount of skepticism.
Ascended. "The holier-than-thou Ascended, come to save us mortals, eh? Well, we don't need saving."
Celestial. "Some claim they've been blessed by a celestial, but since when have they cared for us?"
Golem. "Piles of fancy rocks. I can carve my own weapons, build my own halls, grow my own crops. What would I need them for?"
Humans. “I've met some humans in my travels—cowards, the lot of them, and the rest think themselves brave. They should mind their own rather than stick their fingers in too many pots.”
Spirits. “Never known a trustful spirit. Far too wily, dancing around the forests, thinking they own the place."
Troll. "Humans think us animals? They haven't met the blade of a troll. Trolls hold no regard for precision... or any regard at all."
Vastaya. “Vastaya can be a bit too volatile for my tastes—and that's coming from a cow."

### Minotaur Names

The names of minotaurs are quite guttural in sound, accounting for beast-like vocal chords. However, they are still based in Noxian script and pronunciation. Minotaurs do not typically have surnames, as they do not track lineage as humans do. If they need to identify themselves, they might do so by affixing the name of their clan to their title.

**Male Names:** Anaidax, Dengrim, Erkiras, Huntruk, Morefrad, Rethmek, Syrathun, Trareus, Wryestair, Zhaben

**Female Names:** Andeha, Belrada, Gneveru, Konatia, Mentsis, Phigea, Shesen, Silzera, Vottian, Xamara

**Gender-Neutral Names:** Agsan, Gremerdes, Konden, Lerrenes, Mazeph, Maulivar, Ramonis, Rhosin, Vrivir

### Minotaur Traits

Your Minotaur character has the following traits:

**_Ability Score Increase._** Your Strength score increases by 2, and your Constitution score increases by 1.

**_Age._** Minotaurs age at a somewhat faster rate than humans. They are considered adult at around 15 years, and they can live up to 150 years.

**_Alignment._** Minotaurs vary in alignment. Usually, minotaurs are lawful and loyal to the functions of their clan. However, some have dedicated themselves to causes outside of their kin, such as the noble armies of Demacia or the chaotic fighting pits of Noxus.

**_Size._** Minotaurs stand tall and burly, ranging between 6 to 8 feet on average. Your size is Medium.

**_Speed._** Your base walking speed is 30 feet.

**_Horns._** Your horns are a melee weapon that deals 1d6 + STR piercing damage, and you are proficient with your horns.

**_Charge and Gore._** If you move at least 20 feet straight toward a target, you can then gore it with your horns. On a successful charge and gore, the target takes an extra 2d6 piercing damage.
GORE (Melee Weapon Attack) Proficiency bonus + STR to hit, reach 5 ft, one target. _Hit:_ 1d6 + STR piercing damage.

**_Menacing._** You gain proficiency in the Intimidation skill.

**_Relentless Endurance._** When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest.

**_Stomp._** As an action, you can stomp the ground around you. Each creature within 5 feet of you must make a Dexterity saving throw. A creature falls prone and takes 2d6 bludgeoning damage on a failed save, or half as much damage on a successful one. A creature stays upright on a successful save. A creature that is hovering or flying is not affected.

**_Languages._** You can speak, read, and write Va-Nox and the language of the region from which your clan hails. Minotaur clans are found throughout Runeterra, typically in the mountains of Noxus, the woods of Demacia, or the sea caves around Piltover (so your character might speak Noxian, Demacian, or Piltovan, respectively).

<!--------------- SPIRIT  --------------->

## Spirit

Spirits long precede the existence of human societies and history. Tied intrinsically to realms beyond mortal understanding, spirits are mystical and magical. Spirits draw some sustenance from the mortal world, though that sustenance takes different forms and extents. Demons, for instance, survive on negative aspects of mortal experience, gorging on the resulting manic, charged energy. Meanwhile, Yordles sometimes seek mortal companionship out of natural sociability. In either case, spirits bring supernatural influence to Runeterra.

### Drawn to Emotion

Some spirits, particularly demons, are born directly from mortal emotion—embodying strong, collective feelings like fear, rage, sorrow, or desire. Others might be summoned by arcanists or cultists, and these spirits may then rely on mortal temptation and ensnarement for survival.

Other spirits, like yordles, may come from their enchanted homeland of Bandle City out of admiration or curiosity regarding the physical world. These more pleasant of these spirits tend to be genial, contributing to human societies and advancements. The more unpleasant of these spirits, however, might be more impish and potentially harmful.

### Predator and Prey

For different reasons, spirits are often considered unwelcome in Runeterra's civilizations. Demons are abhorred as horrid predators, and mythos often emerges about these demonic menaces. As such, these spirits rarely engage in human affairs, instead preferring the cover of night to find isolated victims.

Yordles, with their unnatural appearance or their less-than-predictable motives, are frequently considered threats to some human societies. Some extremists have taken to hunting yordles without exception. However, some of these spirits have utilized their magic and ingenuity to create glamours. This allows them to appear much more palatable to society and continue interacting with the mortal world.

### Spirit Names

The names of spirits do not follow the traditional naming conventions of mortals. Demon names typically stem from what mortals might call them, giving their fears or anxieties identity and physical form. Or, a demon might choose a name from past victims, assuming a different name as time goes on. Contrastingly, yordle names tend to sound friendly and welcoming, with double letters or simple syllabic counts.

**Demon Names:** (Demonic names) Asha, Damethus, Faltas, Redmurne, Yeboros; (Names from mortals) Pick a name from the human or vastaya races, based on one such victim.

**Yordle Names:** Bicey, Cheelie, Eearey, Fayan, Grari, Jilni, Ledrey, Meevo, Pimmer, Perret, Wultz, Yorro, Zefo

### Spirit Traits

Your spirit character has the following traits:

**_Ability Score Increase._** Your Charisma score increases by 2.

**_Age._** Spirits age at a much slower rate than humans, and their lifespans are drastically higher, lasting millennia.

**_Alignment._** Spirits can be wily and unpredictable; as such, they are rarely of lawful alignments. Demons are often evil in alignment, while yordles tend toward good.

**_Size._** Spirit forms vary. If you are a demon, your size is Medium. If you are a yordle, your size is Small.

**_Speed._** Your base walking speed is 30 feet.

**_Living Spirit._** You are immune to disease. You do not need to eat, but you can ingest food and drink if you wish. Also, instead of sleeping, you enter a sleep-like state. You need to remain in it for only 4 hours each day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep.

**_Mystical Awareness._** You have advantage on saving throws against being charmed, and magic can’t put you to sleep.

**_Spirit Realm's Refuge._** As an action, you can teleport into a pocket of the Spirit Realm. The pocket is about 20 x 20 feet, and you can remain there for one hour. When the hour ends or when you choose, you teleport back to the exact location you were in prior to entering the Spirit Realm, or in the nearest unoccupied space. Once you use this feature, you cannot use it again until you complete three long rests.

**_Languages._** You can speak, read, and write Va-Nox and Sylvan, the language of the Spirit Realm.

**_Subraces._** Spirits are generally divided into two groups. Demons are malevolent, feasting on the turbulent emotions or desires of mortals. Yordles tend to be more amiable, traversing Runeterra with wellmeant mischief. Choose one of these subraces.

#### Demon

The appearance of a demon differs wildly. Some accounts claim to have seen a humanoid catfish haunting the gambling halls of Bilgewater. Other legends abound of a lustful demoness who takes whatever form her targets find desirable. Less powerful demons might assume a physical form with which to interact with mortals. Upon the destruction of that form, the spirit returns to the Spirit Realm for recuperation.

Unholy dwellers of darkness, demons wander the world in search of mortals to make prey. While the intentions demons hold can be hard to pinpoint, they can be assumed to be evil in nature. After all, their specialty might be in consuming and corrupting souls.

**_Ability Score Increase._** Your Wisdom score increases by 1.

**_Evil Insight._** Once per long rest, you can look into the weaknesses of a creature you can see. As a bonus action, you can target a creature. Make a Wisdom (Insight) check against that creature's Charisma (Deception). Upon success, you gain advantage on the next attack roll against that creature. Also, you learn the creature's damage vulnerabilities, if any.

**_Demonic Darkvision._** Being a demon, you are much accustomed to prowling in the dark. Your darkvision has a radius of 120 feet. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

**_Light Aversion._** You are vulnerable to radiant damage.

#### Yordle

Small and lively, yordles tend to have mammalian features. They have a range of physical characteristics, with male yordles typically appearing more furry while female yordles appearing with smooth, brightly-colored skin.

Yordles may be one of the most misunderstood beings across Runeterra. Some underestimate them as harmless little creatures without their own ambitions. Others drastically overstate the dangers that yordles pose. Somehow, yordles persist, chasing their aspirations, whether that be making technological advancements in the mortal world or causing ruckus in one's wake.

**_Ability Score Increase._** Your Intelligence score increases by 2.

**_Magic Mischief._** Yordles are inherently magical. Once per long rest, you can use your bonus action to do one of the following:
• Impose advantage on the next spell attack by a willing creature other than yourself.• Impose disadvantage on the next enemy spell attack. • Change the damage type of your next successful spell attack.

**_Yordle Ears._** Yordles tend to have large, sometimes fluffy ears. As such, you have advantage on Wisdom (Perception) checks that rely on hearing.

### Spirit converted

name="Spirit",flavor="Spirits long precede the existence of human societies and history. Tied intrinsically to realms beyond mortal understanding, spirits are mystical and magical. Spirits draw some sustenance from the mortal world, though that sustenance takes different forms and extents. Demons, for instance, survive on negative aspects of mortal experience, gorging on the resulting manic, charged energy. Meanwhile, Yordles sometimes seek mortal companionship out of natural sociability. In either case, spirits bring supernatural influence to Runeterra.",descriptions=[("Drawn to Emotion",["Some spirits, particularly demons, are born directly from mortal emotion—embodying strong, collective feelings like fear, rage, sorrow, or desire. Others might be summoned by arcanists or cultists, and these spirits may then rely on mortal temptation and ensnarement for survival.","Other spirits, like yordles, may come from their enchanted homeland of Bandle City out of admiration or curiosity regarding the physical world. These more pleasant of these spirits tend to be genial, contributing to human societies and advancements. The more unpleasant of these spirits, however, might be more impish and potentially harmful."]),("Predator and Prey", ["For different reasons, spirits are often considered unwelcome in Runeterra's civilizations. Demons are abhorred as horrid predators, and mythos often emerges about these demonic menaces. As such, these spirits rarely engage in human affairs, instead preferring the cover of night to find isolated victims.", "Yordles, with their unnatural appearance or their less-than-predictable motives, are frequently considered threats to some human societies. Some extremists have taken to hunting yordles without exception. However, some of these spirits have utilized their magic and ingenuity to create glamours. This allows them to appear much more palatable to society and continue interacting with the mortal world."])],nameDescription="The names of spirits do not follow the traditional naming conventions of mortals. Demon names typically stem from what mortals might call them, giving their fears or anxieties identity and physical form. Or, a demon might choose a name from past victims, assuming a different name as time goes on. Contrastingly, yordle names tend to sound friendly and welcoming, with double letters or simple syllabic counts.",namesData=[("Demonic", "Asha, Damethus, Faltas, Redmurne, Yeboros"),("Yordle", "Bicey, Cheelie, Eearey, Fayan, Grari, Jilni, Ledrey, Meevo, Pimmer, Perret, Wultz, Yorro, Zefo")],nameFormat="{{name}}",traitsDescription="Your spirit character has the following traits:",traitsDescriptions=[("Ability Score Increase", "Your Charisma score increases by 2."),("Age", "Spirits age at a much slower rate than humans, and their lifespans are drastically higher, lasting millennia."),("Alignment", "Spirits can be wily and unpredictable; as such, they are rarely of lawful alignments. Demons are often evil in alignment, while yordles tend toward good."),("Size", "Spirit forms vary. If you are a demon, your size is Medium. If you are a yordle, your size is Small."),("Speed", "Your base walking speed is 30 feet."),("Living Spirit", "You are immune to disease. You do not need to eat, but you can ingest food and drink if you wish. Also, instead of sleeping, you enter a sleep-like state. You need to remain in it for only 4 hours each day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."),("Mystical Awareness", "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."),("Spirit Realm's Refuge", "As an action, you can teleport into a pocket of the Spirit Realm. The pocket is about 20 x 20 feet, and you can remain there for one hour. When the hour ends or when you choose, you teleport back to the exact location you were in prior to entering the Spirit Realm, or in the nearest unoccupied space. Once you use this feature, you cannot use it again until you complete three long rests."),("Languages", "You can speak, read, and write Va-Nox and Sylvan, the language of the Spirit Realm."),("Subraces", "Spirits are generally divided into two groups. Demons are malevolent, feasting on the turbulent emotions or desires of mortals. Yordles tend to be more amiable, traversing Runeterra with wellmeant mischief. Choose one of these subraces.")], traits=[("Living Spirit", "You are immune to disease. You do not need to eat, but you can ingest food and drink if you wish. Also, instead of sleeping, you enter a sleep-like state. You need to remain in it for only 4 hours each day. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."),("Mystical Awareness", "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."),("Spirit Realm's Refuge", "As an action, you can teleport into a pocket of the Spirit Realm. The pocket is about 20 x 20 feet, and you can remain there for one hour. When the hour ends or when you choose, you teleport back to the exact location you were in prior to entering the Spirit Realm, or in the nearest unoccupied space. Once you use this feature, you cannot use it again until you complete three long rests.")],stats=[("charisma", 2)],subraceDescription="Spirits are generally divided into two groups. Demons are malevolent, feasting on the turbulent emotions or desires of mortals. Yordles tend to be more amiable, traversing Runeterra with wellmeant mischief. Choose one of these subraces.",subraces=[{"name":"Demon","desc":"<p>The appearance of a demon differs wildly. Some accounts claim to have seen a humanoid catfish haunting the gambling halls of Bilgewater. Other legends abound of a lustful demoness who takes whatever form her targets find desirable. Less powerful demons might assume a physical form with which to interact with mortals. Upon the destruction of that form, the spirit returns to the Spirit Realm for recuperation.</p><p>Unholy dwellers of darkness, demons wander the world in search of mortals to make prey. While the intentions demons hold can be hard to pinpoint, they can be assumed to be evil in nature. After all, their specialty might be in consuming and corrupting souls.</p>","traitDescs":[("Ability Score Increase", "Your Wisdom score increases by 1."),("Evil Insight", "Once per long rest, you can look into the weaknesses of a creature you can see. As a bonus action, you can target a creature. Make a Wisdom (Insight) check against that creature's Charisma (Deception). Upon success, you gain advantage on the next attack roll against that creature. Also, you learn the creature's damage vulnerabilities, if any."),("Demonic Darkvision", "Being a demon, you are much accustomed to prowling in the dark. Your darkvision has a radius of 120 feet. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),("Light Aversion", "You are vulnerable to radiant damage.")],"traits":[("Evil Insight", "Once per long rest, you can look into the weaknesses of a creature you can see. As a bonus action, you can target a creature. Make a Wisdom (Insight) check against that creature's Charisma (Deception). Upon success, you gain advantage on the next attack roll against that creature. Also, you learn the creature's damage vulnerabilities, if any."),("Demonic Darkvision", "Being a demon, you are much accustomed to prowling in the dark. Your darkvision has a radius of 120 feet. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),("Light Aversion", "You are vulnerable to radiant damage.")],
"stats":[("charisma", 2), ("wisdom", 1)]},{"name":"Yordle",
"desc":"<p>Small and lively, yordles tend to have mammalian features. They have a range of physical characteristics, with male yordles typically appearing more furry while female yordles appearing with smooth, brightly-colored skin.</p><p>Yordles may be one of the most misunderstood beings across Runeterra. Some underestimate them as harmless little creatures without their own ambitions. Others drastically overstate the dangers that yordles pose. Somehow, yordles persist, chasing their aspirations, whether that be making technological advancements in the mortal world or causing ruckus in one's wake.</p>",
"traitDescs":[("Ability Score Increase", "Your Intelligence score increases by 2."),
("Magic Mischief", "Yordles are inherently magical. Once per long rest, you can use your bonus action to do one of the following:<ul><li>Impose advantage on the next spell attack by a willing creature other than yourself.</li><li> Impose disadvantage on the next enemy spell attack.</li><li>Change the damage type of your next successful spell attack.</li></ul>"),("Yordle Ears", "Yordles tend to have large, sometimes fluffy ears. As such, you have advantage on Wisdom (Perception) checks that rely on hearing.")],
"traits":[("Magic Mischief", "Yordles are inherently magical. Once per long rest, you can use your bonus action to do one of the following:<ul><li>Impose advantage on the next spell attack by a willing creature other than yourself.</li><li> Impose disadvantage on the next enemy spell attack.</li><li>Change the damage type of your next successful spell attack.</li></ul>"),("Yordle Ears", "Yordles tend to have large, sometimes fluffy ears. As such, you have advantage on Wisdom (Perception) checks that rely on hearing.")],
"stats":[("charisma", 2), ("intelligence", 2)]}]

<!--------------- TROLL  --------------->

## Troll

Imposing, lumbering creatures, trolls battle for survival in Runeterra's harshest areas. In the worst that the wastelands have to offer, strength reigns supreme: trolls are rigid in their need to suvive. They trample over those perceived as weak, and they relish the routines of raiding, plundering, and hunting.

### Badland Behemoths

Mirroring the rough lands in which they live, trolls' appearances are quite grisly. Ranging between 6 to 8 feet tall, trolls are natural predators in their environments. They also have huge mouths with many sharpened teeth; dull skin tones in blues, greens, and browns; and bulky bodies covered in warts.

Trolls tend to band together in the badlands in local tribes. They haunt the harshest places in commanding groups, using their striking statures and barbaric weapons to take what they need.

### Survival of the Fittest

Trolls may not be Runeterra's smartest—though exceptions exist, as some trolls prove an unexpected amount of intellect and cleverness—but they are certainly Runeterra's hardiest. By necessity, they prioritize survival of the fittest. Most frequently, to be the fittest means to be the largest, the strongest, or the most vicious. These are recognized as signs of a true, tenacious troll, so these trolls are often informally appointed as chiefs.

As a result of living in unforgiving worlds, and lacking in structured societies that prevent bloodshed, it is rare for trolls to live to their full age. In fact, trolls regularly partake in actions that other civilizations deem taboo, such as cannibalism or indiscriminate murder. Ultimately, it takes incredible endurance and stubbornness to survive among trolls.

### Troll Names

Troll names are two syllables long, with simple arrangement and pronunciation. As troll societies are quite primitive, they do not use surnames. This is also due to the fact that the rate of survival is extremely low among trolls, so names are not considered important information to memorize for long.

**Male Names:** Balzim, Detid, Gamja, Hammo, Kaijab, Kelraz, Lagbo, Rabash, Sesdu, Silbo, Tarmek, Vutza, Zulkaz

**Female Names:** Bunjin, Dulyu, Gilta, Helthra, Kritzel, Morgo, Rangi, Rasha, Shakba, Tezza, Wrathro, Yashbi, Zenma

**Gender-Neutral Names:** Boryan, Bruddle, Damar, Madras, Ronja, Teddar, Tizzal, Vannro, Yasho, Zhonlo, Zinjel

### Troll Traits

Your troll character has the following traits:

**_Ability Score Increase._** Your Constitution score increases by 2.

**_Age._** Trolls age at a slower rate than humans. They are considered adult by age 50, and they can live up to 300 to 350 years.

**_Alignment._** Most trolls tend toward neutral or evil. Survival is first and foremost on their minds, but trolls have recently come to relish the practice of war.

**_Size._** Trolls are intimidating in stature, compared to humans. They typically stand between 6 to 8 feet tall. Your size is Medium.

**_Speed._** Your base walking speed is 30 feet.

**_Darkvision._** Accustomed to living in dark areas, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.|

**_Keen Smell._** You have advantage on Wisdom (Perception) checks that rely on smell.

**_Savage Attacks._** When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit.

**_Troll Toughness._** Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.

**_Quick Healing._** As a reaction to you taking damage, you can roll 1d6 + CON and recover that amount of hit points. Once you use this feature, you cannot use it again until you complete a long rest.

**_Languages._** You can speak Va-Nox, but you cannot read nor write it.

**_Subraces._** Trolls are split into two main subraces, based on where they are from: frost-trolls and sand-trolls. Choose one subrace.

#### Frost-Troll

Beyond the boundariess of human civilizations, frost-trolls thrive among the frigid glaciers of the Freljord. In Freljordian villages, parents often tell cautionary tales to their children, warning them of the boogeyman trolls who scavenge among the frozen barrens. There are elements of truth to these stories: frost-trolls have been recorded to attack human settlements in search of food and supplies—and concerningly, to spread their conquest.

Indeed, in recent times, rumors have spread of the frost-trolls rallying under the banner of a single troll—a phenomenon previously unheard of. While these whispers of unification are unconfirmed, however, frost-trolls remain their savage selves: happy to feast and wage war to their hearts' content.

**_Ability Score Increase._** Your Strength score increases by 1.

**_Arctic Terrain Familiarity._** When traveling in arctic terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.

**_Frost-troll Weapon Training._** You have proficiency with mauls, war picks, and warhammers.

#### Sand-Troll

In the deserts of Shurima and the bordering fields of Ixtal, sand-trolls scavenge beneath the sands and trees. They live in extreme secrecy, more so than their frost-troll counterparts. They nonetheless have similar tenacity, thriving in an environment with scarce food sources and bleak weather.

**_Ability Score Increase._** Your Dexterity score increases by 1.

**_Desert Terrain Familiarity._** When traveling in desert terrain, you gain advantage on Wisdom (Survival) checks, and you are not hindered by difficult terrain.

**_Sand-troll Weapon Training._** You have proficiency with greataxes, morningstars, and scimitars.

<!--------------- VASTAYA  --------------->

## Vastaya

Tribes set in the deep wilderness, animalistic features and temperaments, innate connection with Runeterra's magic; the vastayan peoples are unified in these traits. However, the vastaya are diverse and far-reaching, just as the tides of nature itself are chaotic and uncontrollable.

### Blood of the Wild

The vastaya have differing degrees of animal-like features. Some appear more human-like, with few chimeric traits to distinguish them from their mortal peers. Others are fully animal in appearance. Some even develop combinations of distinct animal characteristics, embodying amalgamations of bestial characteristics in a single body.

Depending on the tribe and connection to ancient magic, vastaya have various levels of shapeshifting ability. Most vastaya maintain a shape that incorporates both animal and humanoid features, with special care for matching the animal ancestry of their tribe (for instance, a vastaya of the reptilian Strig tribe would likely retain their reptilian features.)

### Ancient Heritage

Vastaya trace their lineage to ancient times, particularly to the intermingling of humans and a primeval race called the Vastayashai’rei. As legend states, the Vastayashai’rei originated in the First Lands, which would come to be called Ionia. In a primordial war with titans who rained hell from the skies above, the Vastayashai’rei absorbed the land's natural and spiritual magic into their bodies, becoming vastly powerful.

Thousands upon thousands of years after this war, the vastaya emerged as descendants of these ancient peoples. The vastaya evolved into different brances and tribes, forming their own societies, languages, and civilizations across Runeterra. Now, most vastayan tribes reside in Ionia, a land which still carries inherent magic that gives the life to the vastaya.

### Vastaya Names

Vastayan names are typically drawn from the vastayan language, but some might be based in Ionian script. Names are given at birth, by parents or by tribe elders, depending on clan traditions.

**Male Names:** Akrato, Brekan, Draclo, Gongram, Ishkan, Marok, Neyerdan, Redalish, Strago, Vilom, Watong

**Female Names:** Ahlana, Elmi, Hanni, Irroa, Lakaia, Meian, Neirin, Ohrila, Raini, Sedlani, Sheilah, Viyana, Weeva

**Gender-Neutral Names:** Alekhan, Belnani, Halansa, Jerivahn, Mahni, Narene, Rantloa, Songna, Weivam

### Vastaya Traits

Your Vastaya character has the following traits:

**_Ability Score Increase._** Your Wisdom score increases by 2.

**_Age._** Vastaya reach physical maturity at around the same rate as humans, but they stay youthful for longer and have more prolonged lifespans. They can live to be up to 600 years old.

**_Alignment._** Most vastaya care not for the laws of mankind, instead aligning themselves with the chaos of nature and magic. As such, vastaya tend toward chaotic alignments.

**_Size._** Vastaya are comparable in size and weight to humans, ranging between 4 to 6 feet tall, depending on the subrace. Your size is Medium.

**_Speed._** Your base walking speed is 30 feet.

**_Innate Shapechanger._** You can cast the second-level spell _Alter Self,_ without expending a spell slot. Once you cast it, you can't do so again until you finish a long rest.

**_Knowledge of the Wild._** You are proficient in the Nature and Survival skills.

**_Languages._** You can speak, read, and write Va-Nox and Vastayan. The Vastayan language has many dialects originating from the split of different tribes.

**_Subraces._** There are numerous branches of vastayan heritage and forms, but they can be generalized into three tribal groupings: Landwalker Tribes, Tribes of the Sea, and Tribes of the Sky. Choose one such subrace.

#### Landwalker Tribes

As the category suggests, the Landwalker Tribes are made up of vastaya who tread the earth. Generally, Landwalker Tribes are the most numerous and common groups of vastaya found in Runeterra. Landwalker Tribes include branches like the goatlike Fauhwoon, the birdlike Lhotlan, the monkeylike Shimon, and several others.

**_Ability Score Increase._** Your Strength score increases by 1.

**_Climbing Speed._** You have a climbing speed of 30 feet.

**_Innate Spellcasting._** You know the _Druidcraft_ cantrip.

**_Mask of the Wild._** Used to traversing forests and wilds, you can attempt to hide when you are only slightly obscured by folliage, tree bark, or rock walls.

**_Speak with Small Beasts._** Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts.

#### Tribes of the Sea

Tribes of the Sea inhabit Runeterra's seas and oceans, able to survive in depths untouched by humans. As a result of living in the oceans, separate from human intervention, they are the most in-touch with Runeterra's natural magic—flowing in its watery depths. They tend to be the least human-like in appearance, needing aquatic traits like gills and fins to thrive in water environments. Tribes of the Sea include the mermen-like Marai, the Makara, and the Raylu.

**_Ability Score Increase._** Your Charisma score increases by 1.

**_Amphibious._** You can breathe on land and in water.

**_Innate Spellcasting._** You know the _Shape Water_ cantrip.

**_Swimming Speed._** You have a swimming speed of 30 feet.

**_Sea Weapon Training._** You have proficiency with spears, tridents, and nets.

#### Tribes of the Sky

Tribes of the Sky vastaya live far above the lands of humans, in the skies, trees, and mountains. Tribes of the Sky include the Besheb, the Strig, the Chyra, and other unidentified tribes.

**_Ability Score Increase._** Your Dexterity score increases by 1.

**_Innate Spellcasting._** You know the _Gust_ cantrip.

**_Talons._** Your have talons, which can act as natural weapons and be used to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Dexterity modifier, instead of the bludgeoning damage normal for an unarmed strike.

**_Wings._** You have a flying speed of 30 feet. You must be in a space wide enough to accommodate your wingspan to fly. Your wingspan is equal to twice your height. You cannot fly if you are wearing armor you are not proficient in, armor not tailored to accommodate your wings, or a backpack not specially tailored to your wings.
