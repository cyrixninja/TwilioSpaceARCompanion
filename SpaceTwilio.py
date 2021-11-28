from datetime import time
import re
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'earth' in incoming_msg:
        msg.media('https://cdn.mos.cms.futurecdn.net/3upZx2gxxLpW7MBbnKYQLH-1200-80.jpg')
        msg.body("https://go.echo3d.co/jKwV")
        msg.body("Our home planet is the third planet from the Sun, and the only place we know of so far that’s inhabited by living things.While Earth is only the fifth largest planet in the solar system, it is the only world in our solar system with liquid water on the surface. Just slightly larger than nearby Venus, Earth is the biggest of the four planets closest to the Sun, all of which are made of rock and metal.The name Earth is at least 1,000 years old. All of the planets, except for Earth, were named after Greek and Roman gods and goddesses. However, the name Earth is a Germanic word, which simply means the ground.")
    if 'mars' in incoming_msg:
        msg.media('https://mars.nasa.gov/system/content_pages/main_images/418_marsglobe.jpg')
        msg.body("https://go.echo3d.co/GU2a")
        msg.body("Mars is the fourth planet from the Sun – a dusty, cold, desert world with a very thin atmosphere. Mars is also a dynamic planet with seasons, polar ice caps, canyons, extinct volcanoes, and evidence that it was even more active in the past.Mars is one of the most explored bodies in our solar system, and it's the only planet where we've sent rovers to roam the alien landscape.")
    if 'venus' in incoming_msg:
        msg.media('https://upload.wikimedia.org/wikipedia/commons/0/08/Venus_from_Mariner_10.jpg')
        msg.body("https://go.echo3d.co/GQPd")
        msg.body("Venus is the second planet from the Sun and is Earth’s closest planetary neighbor. It’s one of the four inner, terrestrial (or rocky) planets, and it’s often called Earth’s twin because it’s similar in size and density. These are not identical twins, however – there are radical differences between the two worlds.Venus has a thick, toxic atmosphere filled with carbon dioxide and it’s perpetually shrouded in thick, yellowish clouds of sulfuric acid that trap heat, causing a runaway greenhouse effect. It’s the hottest planet in our solar system, even though Mercury is closer to the Sun. Surface temperatures on Venus are about 900 degrees Fahrenheit (475 degrees Celsius) – hot enough to melt lead. The surface is a rusty color and it’s peppered with intensely crunched mountains and thousands of large volcanoes. Scientists think it’s possible some volcanoes are still active.Venus has crushing air pressure at its surface – more than 90 times that of Earth – similar to the pressure you'd encounter a mile below the ocean on Earth.")
    if 'mercury' in incoming_msg:
        msg.media('https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg')
        msg.body("https://go.echo3d.co/rFML")
        msg.body("The smallest planet in our solar system and nearest to the Sun, Mercury is only slightly larger than Earth's Moon.From the surface of Mercury, the Sun would appear more than three times as large as it does when viewed from Earth, and the sunlight would be as much as seven times brighter. Despite its proximity to the Sun, Mercury is not the hottest planet in our solar system – that title belongs to nearby Venus, thanks to its dense atmosphere.Because of Mercury's elliptical – egg-shaped – orbit, and sluggish rotation, the Sun appears to rise briefly, set, and rise again from some parts of the planet's surface. The same thing happens in reverse at sunset.")
    if 'jupiter' in incoming_msg:
        msg.media('https://upload.wikimedia.org/wikipedia/commons/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg')
        msg.body("https://go.echo3d.co/iBdp")
        msg.body("Jupiter has a long history of surprising scientists – all the way back to 1610 when Galileo Galilei found the first moons beyond Earth. That discovery changed the way we see the universe.Fifth in line from the Sun, Jupiter is, by far, the largest planet in the solar system – more than twice as massive as all the other planets combined.Jupiter's familiar stripes and swirls are actually cold, windy clouds of ammonia and water, floating in an atmosphere of hydrogen and helium. Jupiter’s iconic Great Red Spot is a giant storm bigger than Earth that has raged for hundreds of years.") 
    if 'moon' in incoming_msg:
        msg.media('https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2001/07/view_of_the_moon_seen_apollo_17/9215843-5-eng-GB/View_of_the_Moon_seen_Apollo_17_pillars.jpg')
        msg.body("https://go.echo3d.co/BAvD")
        msg.body("Earth's Moon is the only place beyond Earth where humans have set foot.The brightest and largest object in our night sky, the Moon makes Earth a more livable planet by moderating our home planet's wobble on its axis, leading to a relatively stable climate. It also causes tides, creating a rhythm that has guided humans for thousands of years. The Moon was likely formed after a Mars-sized body collided with Earth.Earth's Moon is the fifth largest of the 200+ moons orbiting planets in our solar system.Earth's only natural satellite is simply called the Moon because people didn't know other moons existed until Galileo Galilei discovered four moons orbiting Jupiter in 1610.")
    if 'sun' in incoming_msg:
        msg.media('https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg/220px-The_Sun_by_the_Atmospheric_Imaging_Assembly_of_NASA%27s_Solar_Dynamics_Observatory_-_20100819.jpg')
        msg.body("https://go.echo3d.co/qjFF")
        msg.body("The sun is a star, a hot ball of glowing gases at the heart of our solar system. Its influence extends far beyond the orbits of distant Neptune and Pluto. Without the sun's intense energy and heat, there would be no life on Earth. And though it is special to us, there are billions of stars like our sun scattered across the Milky Way galaxy. If the sun were as tall as a typical front door, the Earth would be the size of a U.S. nickel. The temperature at the sun's core is about 27 million degrees Fahrenheit.")
    if 'neptune' in incoming_msg:
        msg.media('https://solarsystem.nasa.gov/system/feature_items/images/82_carousel_neptune_1.jpg')
        msg.body("https://go.echoar.xyz/ic6X")
        msg.body("Dark, cold, and whipped by supersonic winds, ice giant Neptune is the eighth and most distant planet in our solar system.more than 30 times as far from the Sun as Earth, Neptune is the only planet in our solar system not visible to the naked eye and the first predicted by mathematics before its discovery. In 2011 Neptune completed its first 165-year orbit since its discovery in 1846.")
    if 'uranus' in incoming_msg:
        msg.media('https://ychef.files.bbci.co.uk/976x549/p0257vk5.jpg')
        msg.body("https://go.echo3d.co/DGQM")
        msg.body("Uranus is the seventh planet from the Sun, and has the third-largest diameter in our solar system. It was the first planet found with the aid of a telescope, Uranus was discovered in 1781 by astronomer William Herschel, although he originally thought it was either a comet or a star.It was two years later that the object was universally accepted as a new planet, in part because of observations by astronomer Johann Elert Bode. Herschel tried unsuccessfully to name his discovery Georgium Sidus after King George III. Instead, the scientific community accepted Bode's suggestion to name it Uranus, the Greek god of the sky, as suggested by Bode.​")
    if 'rover' in incoming_msg:
        msg.media('https://mars.nasa.gov/system/feature_items/images/6037_msl_banner.jpg')
        msg.body("https://go.echo3d.co/2prH")
        msg.body("Curiosity carries the biggest, most advanced instruments for scientific studies ever sent to the Martian surface. The history of Martian climate and geology is written in the chemistry and structure of the rocks and soil. Curiosity reads this record by analyzing powdered samples drilled from rocks. It also measures the chemical fingerprints present in different rocks and soils to determine their composition and history, especially their past interactions with water.")
    if 'saturn' in incoming_msg:
        msg.media('https://cdn.hswstatic.com/gif/saturn-lead-image.jpg')
        msg.body("https://go.echoar.xyz/hjBT")
        msg.body("Saturn is the sixth planet from the Sun and the second-largest planet in our solar system.Adorned with thousands of beautiful ringlets, Saturn is unique among the planets. It is not the only planet to have rings – made of chunks of ice and rock – but none are as spectacular or as complicated as Saturn's.Like fellow gas giant Jupiter, Saturn is a massive ball made mostly of hydrogen and helium.")
    if 'pluto' in incoming_msg:
        msg.media('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Pluto-01_Stern_03_Pluto_Color_TXT.jpg/1200px-Pluto-01_Stern_03_Pluto_Color_TXT.jpg')
        msg.body("https://go.echo3d.co/KtvW")
        msg.body("Pluto is a dwarf planet in the Kuiper Belt, a donut-shaped region of icy bodies beyond the orbit of Neptune. There may be millions of these icy objects, collectively referred to as Kuiper Belt objects (KBOs) or trans-Neptunian objects (TNOs), in this distant region of our solar system.Pluto – which is smaller than Earth’s Moon – has a heart-shaped glacier that’s the size of Texas and Oklahoma. This fascinating world has blue skies, spinning moons, mountains as high as the Rockies, and it snows – but the snow is red.")
    if 'aquarius' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/AquariusCC.jpg')
        msg.body("While one of the biggest, most famous, and oldest named constellations, Aquarius is faint and often hard to find/see. In Greek mythology, Aquarius represented Ganymede, a very handsome young man. Zeus recognized the lad’s good looks, and invited Ganymede to Mt. Olympus to be the cupbearer of the gods. For his service he was granted eternal youth, as well as a place in the night sky. Despite its prominent position and large size, you can see that Aquarius doesn’t really have defining features, nor does it contain any bright stars. The protruding line to the right is Aquarius’s right arm, with the large downward shape being a combination of the water flowing down out of the vase and his right leg. While not the entire constellation, what’s drawn above is what you’re most likely to see in the night sky. You won’t see this one in the city; you’ll need a dark sky to find the cupbearer.")
    if 'aquila' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/AquilaCC.jpg')
        msg.body("Aquila was the eagle that in Greek mythology actually bore Ganymede (Aquarius) up to Mt. Olympus. The eagle was also the thunderbolt carrier for Zeus. This constellation lies in the Milky Way band, and its most prominent star is Altair, which is actually one of the closest naked eye stars to the earth. The top portion of Aquila forms a shallow inverted “V,” with Altair nearly the point. This represents the head and wings of the eagle. A line then descends from Altair, which forms the body of the eagle.Look towards the southern sky in the late summer, near the Milky Way band, for Aquila.")
    if 'aries' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/AriesCC.jpg')
        msg.body("While many constellations have gone through various iterations of mythological stories, Aries has always been the ram. This constellation is one of 12 constellations that form the zodiac — the constellations that straddle the sun’s path across the sky (known in scienctific terms as the ecliptic). In ancient times, that gave the constellations of the zodiac special significance.In Greek mythology, Aries is the ram whose fleece became the Golden Fleece. The Golden Fleece is a symbol of kingship and authority, and plays a significant role in the tale of Jason and the Argonauts. Jason is sent to find the fleece in order to rightfully claim his throne as king, and with some help from Medea (his future wife), finds his prize. It’s one of the oldest stories in antiquity, and was current in Homer’s time.")
    if 'canis major' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/CanisMajorCC.jpg')
        msg.body("Canis Major represents the famed Greek dog Laelaps. There are a few origin stories, but the common theme is that he was so fast he was elevated to the skies by Zeus. Laelaps is also considered to be one of Orion’s hunting dogs, trailing behind him in the night sky in pursuit of Taurus the bull. Canis Major is notable because it contains the brightest star in the night sky, Sirius. Tradition notes that the first appearance of Canis Major in the dawn sky comes in late summer, ushering in the dog days of the season. In the night sky, it almost looks a stick figure, with Sirius at the head, and another bright star, Adhara, at its rear end.")
    if 'cassiopeia' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/CassiopeiaCC.jpg')
        msg.body("Cassiopeia, in Greek mythology, was a vain queen who often boasted about her beauty. She was the mother of Princess Andromeda, and in contrast to other figures being placed in the sky in honor, Cassiopeia was forced to the heavenly realms as punishment. As the story goes, she boasted that her beauty (or her daughter’s, depending on the story) was greater than that of the sea nymphs. This was quite an offense, and she was banned to the sky for all to gawk at.With its distinctive “W” shape formed by five bright stars, Cassiopeia is one of the most easily recognizable constellations in the night sky come fall and early winter. And because of that, the vain queen is one of the most oft-mentioned in pop culture and one of the earliest constellations that young children come to recognize in the sky.")
    if 'cygnus' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/CygnusCC.jpg')
        msg.body("Multiple personas take on the form of the swan in Greek mythology. At one point Zeus morphed into a swan to seduce Leda, mother of both Gemini and Helen of Troy. Another tale says that Orpheus was murdered and then placed into the sky as a swan next to his lyre (the constellation Lyra, also in the drawing above).The constellation may also have gotten its name from the tale of Phaethon and Cycnus. Phaethon was the son of Helios (the sun god), and took his father’s sun chariot for a ride one day. Phaethon couldn’t control the reins, however, and Zeus had to shoot down the chariot with Phaethon in it, killing him. Phaethon’s brother, Cycnus (now spelled Cygnus), spent many days grieving and collecting the bones, which so touched the gods that they turned him into a swan and gave him a place in the sky.The Northern Cross is really just an asterism (recognizable pattern of stars) within Cygnus the swan. Deneb, the swan’s tail (or top point of the cross), is one of the brightest stars in the night sky. You’ll find Cygnus within the Milky Way, which is why you’ll sometimes see the constellation referred to as the backbone of the galaxy. In the night sky, the goose is looking down with its wings spread out parallel to the horizon.")
    if 'gemini' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/GeminiCC.jpg')
        msg.body("Gemini represents the twins Castor and Pollux. While the twins’ mother was Leda, Castor’s father was the mortal king of Sparta, while Pollux’s father was King Zeus (He seduced Leda in the form of a swan, remember? These stories tend to all tie together!). When Castor was killed, the immortal Pollux begged Zeus to give Castor immortality, which he did by placing the brothers in the night sky for all time.Castor and Pollux also happen to be the names of the brightest stars in the constellation, and represent the heads of the twins. Each star then has a line forming their bodies, giving the constellation a rough “U” shape. The twins sit next to Orion, making them fairly easy to find in winter.")
    if 'leo' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/LeoCC.jpg')
        msg.body("Leo has been a great lion in the night sky across almost all mythological traditions. In Greek lore, Leo is the monstrous lion that was killed by Hercules as part of his twelve labors. The lion could not be killed by mortal weapons, as its fur was impervious to attack, and its claws sharper than any human sword. Eventually Hercules tracked him down and strangled the great beast, albeit losing a finger in the process.Because Leo actually looks somewhat like its namesake, it is the easiest constellation in the zodiac to find. A distinctive backwards question mark forms the head and chest, then moves to the left to form a triangle and the lion’s rear end. Regulus is Leo’s brightest star, and sits in the bottom right of the constellation, representing the lion’s front right leg.")
    if 'lyra' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/LyraCC.jpg')
        msg.body("Lyra is associated with the myth of Orpheus the great musician (remember him from earlier?). Orpheus was given the harp by Apollo, and it’s said that his music was more beautiful than that of any mortal man. His music could soothe anger and bring joy to weary hearts. Wandering the land in depression after his wife died, he was killed and his lyre (harp) was thrown into a river. Zeus sent an eagle to retrieve the lyre, and it was then placed in the night sky.Lyra sort of forms a lopsided square with a tail to its brightest star, Vega, which is one of the brightest stars in the sky. It is small, and almost directly overhead in the summer months, but the bright Vega makes it fairly easy to find.")
    if 'orion' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/OrionCC.jpg')
        msg.body("Orion is one of the largest and most recognizable of the constellations. It is viewable around the world, and has been mentioned by Homer, Virgil, and even the Bible, making it perhaps the most famous constellation.Orion was a massive, supernaturally gifted hunter who was the son of Poseidon. It was said he regularly hunted with Artemis (Goddess of the Hunt) on the island of Crete, and that he was killed either by her bow, or by the sting of the great scorpion who later became the constellation Scorpius.Orion’s belt of three stars is the easiest asterism to find, with Rigel (bottom right) and Betelgeuse (top left) being the brightest two individual stars. The two other corners form a rough quadrangle, with his head and bow also sometimes visible. Orion is also unique in that you can use him to find a variety of other constellations in the winter sky.")
    if 'pisces' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/PiscesCC.jpg')
        msg.body("The two fish of the sky represent Aphrodite and her son Eros, who turned themselves into fish and tied themselves together with rope in order to escape Typhon, the largest and most vile monster in all of Greek mythology.It’s not likely you’ll find Pisces in the middle of a city, as none of its individual stars are really worth noting or particularly bright. It forms a large “V” with the right fish forming a small “O” on the end, and the left fish forming a small triangle on the end (the image above doesn’t connect the dots in the upper left to make it a triangle).")
    if 'scorpius' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/Scorpius_rising.jpeg')
        msg.body("There are a variety of myths associated with the scorpion, almost all of them involving Orion the hunter. Orion once boasted that he could kill all the animals on the earth. He encountered the scorpion, and after a long, fierce fight, Orion was defeated. It was such a hard-fought battle that it caught the eye of Zeus, and the scorpion was raised to the night sky for all eternity.With many bright stars, Scorpius is fairly easy to find in the night sky. Antares, the brightest star in the constellation, is said to be the heart of the scorpion. That will be the easiest star to locate, but is sometimes confused with Mars because of its red-orange coloring. To the right of the heart are 3-5 stars that form the head. To the left are a long line of stars that curve into a sideways or upside-down question mark.")
    if 'taurus' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/TaurusCC.jpg')
        msg.body("Taurus is a large and prominent fixture in the winter sky. As one of the oldest recognized constellations, it has mythologies dating back to the early Bronze Age. There are several Greek myths involving Taurus. Two of them include Zeus, who either disguised himself as a bull or disguised his mistress as a bull in multiple escapades of infidelity. Another myth has the bull being the 7th labor of Hercules after the beast wreaked havoc in the countryside.The constellation is fairly easy to find as its most recognizable asterism forms a very prominent “V,” which represent the head and horns of the bull. The brightest star in the constellation is Aldebaran, which forms the bull’s right eye. Five stars, fairly close together to the naked eye, form an almost perfect small “V,” with the “V” extending up quite a ways to two more final stars that are the points of the horns.")
    if 'ursa major' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/UrsaMajorCC.jpg')
        msg.body("The Big Dipper is popularly thought of as a constellation itself, but is in fact an asterism within the constellation of Ursa Major. It is said to be the most universally recognized star pattern, partially because it’s always visible in the northern hemisphere. It has great significance in the mythologies of multiple cultures around the world.The Greek myth of Ursa Major also tells the story of Ursa Minor (below). Zeus was smitten for a young nymph named Callisto. Hera, Zeus’s wife, was jealous, and transformed Callisto into a bear. While in animal form, Callisto encountered her son Arcas. Being the man that he was, he was inclined to shoot the bear, but Zeus wouldn’t let that happen, and so turned Arcas into a bear as well, and placed mother (Ursa Major) and son (Ursa Minor) permanently in the night sky.The seven stars of the Big Dipper are easily recognized and almost always visible. They form part of the backside and tail of the large bear. While the rest of the bear definitely takes the shape of its namesake, it’s not often visible in light polluted areas. The Big Dipper is more than just a pretty shape; the outer edge of its “bowl” will always lead you to the North Star, aiding in navigation for centuries past. Simply make a line with the two stars of the Big Dipper’s outer edge, extend that line up into the sky, and at about five times the distance between the two stars you started with, you’ll find the North Star.")
    if 'ursa minor' in incoming_msg:
        msg.media('https://content.artofmanliness.com/uploads/2014/07/UrsaMinorCC.jpg')
        msg.body("Ursa Minor is famous for containing Polaris, the North Star. Many people erroneously think that the North Star is directly over their heads, but that’s only true at the North Pole. For most people in the Northern Hemisphere, it will be dipped into the night sky.Ursa Minor is better known as the Little Dipper. It’s visualized as a baby bear, with an unusually long tail. It can be distinguished from the Big Dipper not only by size, but by the emphasized curvature of the tail. When you’ve found the North Star at the end of the bear’s tail using the Big Dipper, it’s then easy to identify the rest of the constellation.")
    if 'help' in incoming_msg:
        msg.body("""
List  of available Celestial Bodies
1.Mercury
2.Venus
3.Earth
4.Mars
5.Jupiter
6.Saturn
7.Uranus
8.Neptune
9.Pluto
10.Moon
11.Sun
12.Mars Rover
List  of available Constellations
1.Aquarius
2.Aquila
3.Aries
4.Canis Major
5.Cassiopeia
6.Cygnus
7.Gemini
8.Leo
9.Lyra
10.Orion
11.Pisces
12.Scorpius
13.Taurus
14.Ursa Major
15.Ursa Minor
        """)
    return str(resp)    

if __name__ == '__main__':
    app.run()