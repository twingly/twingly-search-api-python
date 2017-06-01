# coding: utf-8

from __future__ import unicode_literals

import unittest

import twingly_search
from twingly_search import Post


class ParserTest(unittest.TestCase):
    def get_fixture(self, fixture_name):
        file_path = "./tests/fixtures/%s.xml" % fixture_name
        fixture = open(file_path, 'r').read()
        return fixture

    def assert_blog_posts_equal(self, actual_post, expected_post):
        self.assertEqual(actual_post.id, expected_post.id)
        self.assertEqual(actual_post.author, expected_post.author)
        self.assertEqual(actual_post.url, expected_post.url)
        self.assertEqual(actual_post.title, expected_post.title)
        self.assertEqual(actual_post.text, expected_post.text)
        self.assertEqual(actual_post.language_code, expected_post.language_code)
        self.assertEqual(actual_post.location_code, expected_post.location_code)
        self.assertEqual(actual_post.coordinates, expected_post.coordinates)
        self.assertEqual(actual_post.latitude, expected_post.latitude)
        self.assertEqual(actual_post.longitude, expected_post.longitude)
        self.assertEqual(actual_post.links, expected_post.links)
        self.assertEqual(actual_post.tags, expected_post.tags)
        self.assertEqual(actual_post.images, expected_post.images)
        self.assertEqual(actual_post.indexed_at, expected_post.indexed_at)
        self.assertEqual(actual_post.published_at, expected_post.published_at)
        self.assertEqual(actual_post.reindexed_at, expected_post.reindexed_at)
        self.assertEqual(actual_post.inlinks_count, expected_post.inlinks_count)
        self.assertEqual(actual_post.blog_id, expected_post.blog_id)
        self.assertEqual(actual_post.blog_name, expected_post.blog_name)
        self.assertEqual(actual_post.blog_url, expected_post.blog_url)
        self.assertEqual(actual_post.blog_rank, expected_post.blog_rank)
        self.assertEqual(actual_post.authority, expected_post.authority)

    def test_with_incomplete_result(self):
        data = self.get_fixture("incomplete_result")
        r = twingly_search.Parser().parse(data)

        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 0)
        self.assertEqual(r.number_of_matches_total, 0)
        self.assertEqual(r.number_of_matches_returned, 0)
        self.assertEqual(r.seconds_elapsed, 0.203)
        self.assertEqual(r.incomplete_result, True)

    def test_with_minimal_valid_result(self):
        self.maxDiff = None
        data = self.get_fixture("minimal_valid_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        posts = r.posts
        self.assertEqual(len(posts), 3)
        self.assertEqual(r.number_of_matches_total, 3122050)
        self.assertEqual(r.number_of_matches_returned, 3)
        self.assertEqual(r.seconds_elapsed, 0.369)
        self.assertEqual(r.incomplete_result, False)

        first_expected_post = Post()
        first_expected_post.set_values(
            {
                "id": "16405819479794412880",
                "author": "klivinihemligheten",
                "url": "http://nouw.com/klivinihemligheten/planering---men-dalig-30016048",
                "title": "Planering - men dålig",
                "text": """Det vart en förmiddag på boxen med en brud som jag lärt känna där. Körde en egen WOD, bland annat SDHP,
            shoulder press, HSPU - bland annat. Hade planerat dagen in i minsta detalj, insåg under passet att jag glömt
            leggings. Så - det var bara att sluta lite tidigare för att röra sig hemåt för dusch och lunch. Har alltså
            släpat med mig ryggsäcken med allt för dagen i onödan. Riktigt riktigt klantigt! Har nu en timma på mig att
            duscha och göra mig ordning för föreläsning, innan det är dags att dra igen. Och jag som skulle plugga innan
        """,
                "languageCode": "sv",
                "locationCode": "se",
                "tags": [
                    "Ätas & drickas",
                    "Universitet & studentlivet",
                    "Träning",
                    "To to list"
                ],
                "indexedAt": "2017-05-04T06:51:23Z",
                "publishedAt": "2017-05-04T06:50:59Z",
                "reindexedAt": "2017-05-04T08:51:23Z",
                "inlinksCount": "0",
                "blogId": "5312283800049632348",
                "blogName": "Love life like a student",
                "blogUrl": "http://nouw.com/klivinihemligheten",
                "blogRank": "1",
                "authority": "0"
            }
        )
        self.assert_blog_posts_equal(posts[0], first_expected_post)

        second_expected_post = Post()
        second_expected_post.set_values({
            "id": "4331268749726303987",
            "author": "berggrenjulia",
            "url": "http://nouw.com/berggrenjulia/sometimes-the-king-is-a-queen-30014929",
            "title": "Sometimes the king is a queen",
            "text": """Dress / Jumpsuit Hej kompisar! Jag satte ihop två söta plagg till er. Himla gölliga! Jag kan inte fatta
            att det är torsdag idag, det är ju helt sjukt. Vid lunch skall jag till läkaren och W följer med mig pga är
            så rädd för läkaren, får brutal ångest och tror att jag skall bli dödförklarad. Riktigt hypokondrisk blir
            man visst med åren. Usch! Känslan när man går därifrån gör dock att det känns värt det. I helgen funderar vi
            på att gå till Liseberg för det skall bli magiskt väder. Vilken tur för alla bal-peppade kompisar på
            Marstrand! Åh dom kommer ha det fantastiskt kul tror jag. För min egen del måste jag erkänna att jag för
            första gången just nu känner att det skall bli skönt att inte gå. Att få slippa hetsen runt omkring då jag
            blir lite stressad bara av att tänka på det. Har verkligen bromsat ner mitt fest-mode rejält och inte varit
            ute och klubbat på superlänge, är inte speciellt lockad alls. Det är alltid samma visa också, så man kan ju
            trösta sig med att man inte missar någonting. Hur ser eran helg ut? Puss!
        """,
            "languageCode": "sv",
            "locationCode": "se",
            "links": [
                "http://www.mtpc.se/tags/link/1008098",
                "http://www.mtpc.se/tags/link/1008099"
            ],
            "tags": [
                "Inspiration",
                "Mode",
                "Vardag"
            ],
            "indexedAt": "2017-05-04T06:51:23Z",
            "publishedAt": "2017-05-04T06:50:00Z",
            "reindexedAt": "2017-05-04T08:51:23Z",
            "inlinksCount": "0",
            "blogId": "9763611270004865418",
            "blogName": "berggrenjulia blogg",
            "blogUrl": "http://nouw.com/berggrenjulia",
            "blogRank": "1",
            "authority": "5"
        })
        self.assert_blog_posts_equal(posts[1], second_expected_post)

        third_expected_post = Post()
        third_expected_post.set_values({
            "id": "2770252465384762934",
            "author": "maartiinasvardag",
            "url": "http://nouw.com/maartiinasvardag/god-formiddag-30016041",
            "title": "God förmiddag! ☀️",
            "text": """Hmm.... Vad ska man börja ?? Jag vet inte riktigt vad min gnista till att blogga har tagit vägen. Jag har
            egentligen massor att skriva om, men ändå blir det inte av att jag gör det. Varför är det så? Någon som
            känner likadant. Kan berätta lite om förra helgen iaf, jag & R åkte till Skövde en sväng på fredagen,
            det blev en hel dag där. Blev en hel del shoppande för oss båda, bilder kommer i ett annat inlägg, då jag
            sitter vid plattan i skrivandets stund. Lördagen var jag hemma med töserna medans R jobbade några timmar.
            Sen blev det bara en lugn kväll hemma. Söndagen så var det dags för mig att jobba, ett dygnspass. ✌️Var en
            lugn kväll på jobbet. På morgonen (måndag) så när jag kommer upp, yrvaken som man är innan första koppen
            kaffe är intagen. Möts jag av att en klient utbrister: Vad glad jag är av att se dig! Detta värmde mitt
            hjärta så oerhört mycket & jag var på strålande humör hela dagen. ❤️ För då vet man att man gör ett bra
            jobb & att man gör rätt för den enskilde klientens behov. Jag älskar mitt jobb, även om jag ibland
            tycker att det är väldigt tufft, men när man får bekräftat att man gjort ett bra jobb, då glömmer man allt
            som är jobbigt. Tisdagen tillbringade jag med att göra ingenting typ, var bara hemma med töserna, solade
            & busade. Satt på baksidan & tjötade med Jonna vid staketet. Ulrika var förbi på en kopp kaffe med
            innan det var dags för henne att åka & jobba. På kvällen blev det sällskapsspel med Nina & Jonna.
            Mycket trevligt. Onsdag blev det lite grejande hemma med att tvätta & plocka lite, tjöta med Jonna i
            vanlig ordning vid staketet. På kvällen blev det ett gympass med Nina & Jonna. ✌️Sen blev det soffan för
            mig & kolla klart på serien Tretton skäl varför. En bra med tung serie där en tjej berättar varför hon
            valde att ta sitt liv. ☹️ Det som skrämmer mig är att det är så här verkligheten ser ut, när det sprids så
            mycket hat. Hur vore det om man började sprida mer kärlek till varandra, acceptera att vi alla är olika
            m.m.? Ja det är nog en fråga som vi aldrig kommer att få svar på. Idag blir det att åka in till stan under
            dagen på lite ärenden, annars är det de gamla vanliga på schemat. Vardags sysslor & R kommer hem, ingen
            är gladare än jag & töserna att få hem honom. ❤️ Önskar er alla en toppen dag! ☀️
        """,
            "languageCode": "sv",
            "locationCode": "se",
            "indexedAt": "2017-05-04T06:50:07Z",
            "publishedAt": "2017-05-04T06:49:50Z",
            "reindexedAt": "0001-01-01T00:00:00Z",
            "inlinksCount": "0",
            "blogId": "1578135310841173675",
            "blogName": "maartiinasvardag blogg",
            "blogUrl": "http://nouw.com/maartiinasvardag",
            "blogRank": "1",
            "authority": "0"
        })
        self.assert_blog_posts_equal(posts[2], third_expected_post)

    def test_with_valid_empty_result(self):
        data = self.get_fixture("valid_empty_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(len(r.posts), 0)
        self.assertEqual(r.number_of_matches_total, 0)
        self.assertEqual(r.number_of_matches_returned, 0)
        self.assertEqual(r.seconds_elapsed, 0.203)
        self.assertEqual(r.incomplete_result, False)

    def test_with_nonexistent_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglySearchClientException) as cm:
            data = self.get_fixture("nonexistent_api_key_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '40001')
        self.assertEqual(error.message, 'Parameter apikey may not be empty')

    def test_with_unauthorized_api_key_result(self):
        with self.assertRaises(twingly_search.TwinglySearchAuthenticationException) as cm:
            data = self.get_fixture("unauthorized_api_key_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '40101')
        self.assertEqual(error.message, 'Unauthorized')

    def test_with_service_unavailable_result(self):
        with self.assertRaises(twingly_search.TwinglySearchServerException) as cm:
            data = self.get_fixture("service_unavailable_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '50301')
        self.assertEqual(error.message, 'Authentication service unavailable')

    def test_with_undefined_error_result(self):
        with self.assertRaises(twingly_search.TwinglySearchServerException) as cm:
            data = self.get_fixture("undefined_error_result")
            r = twingly_search.Parser().parse(data)
        ex = cm.exception
        error = ex.error
        self.assertEqual(error.code, '50001')
        self.assertEqual(error.message, 'Internal Server Error')

    def test_with_non_xml_result(self):
        with self.assertRaises(twingly_search.TwinglySearchException):
            data = self.get_fixture("non_xml_result")
            r = twingly_search.Parser().parse(data)

    def test_valid_links_result(self):
        self.maxDiff = None
        data = self.get_fixture("valid_links_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        posts = r.posts
        self.assertEqual(len(posts), 1)
        self.assertEqual(r.number_of_matches_total, 29383)
        self.assertEqual(r.number_of_matches_returned, 1)
        self.assertEqual(r.seconds_elapsed, 0.413)
        self.assertEqual(r.incomplete_result, False)

        expectedPost = Post()
        expectedPost.set_values({
            "id": "15420612957445610214",
            "author": "Cornucopia?",
            "url": "http://cornucopia.cornubot.se/2017/02/har-ryssland-brutit-mot.html",
            "title": "Har Ryssland brutit mot kärnvapenprovstoppet?",
            "text": """USA verkar ha ombaserat sitt ena i kärnvapenprovdetekteringsplan Constant Phoenix till Europa. Samtidigt
            har nivåer av den med mänskligt ursprung joniserande isotopen Jod-131 detekterats, ursprungligen i
            Nordnorge, som ligger närmast Rysslands gamla kärnvapentestområden i Novaja Semlja. Det väcker frågan om
            Ryssland börjat testa kärnvapen igen? Sovjetunionens första kärnvapenprov.Jod-131 har mänskligt ursprung,
            och är en isotop som uppstår vid detonation av Uran-235 eller plutoniumbaserade kärnvapen. Den har nu
            uteslutande i partikelform detekterats i inledningsvis Nordnorge närmast gränsen mot Ryssland enligt franska
            strålskyddsinstitutet och sedan bland annat i norra Finland och ner över resten av Europa. Nordnorge är som
            bekant närmast Rysslands gamla kärnvapenprovområden vid t ex Novaja Semlja. Jod-131 har en kort
            halveringstid och ursprunget ligger därför i närtid. Ursprunget för isotoperna är i detta fall än så länge
            okänt, och det är också ovanligt att de endast förekommer i partikelform och inte även i gasform. Samtidigt
            verkar nu USA ombaserat en av sina två kärnvapenprovdetekteringsplan Constant Phoenix till Wales.One of the
            two WC-135C CONSTANT PHOENIX Nuclear detonation research aircraft heading towards Wales. Rebasing to UK?
            pic.twitter.com/2P4IDmovzH— S2 Intel (@Strat2Intel) February 17, 2017Flygplanstypen används för att uppe i
            atmosfären detektera spår av kärnvapendetonationer, till skillnad mot mätstationerna som det franska
            strålskyddsinstitutet rapporterar om, som är markbaserade. Det är inte orimligt att man vill söka av högre
            atmosfär efter spår av ett kärnvapenprov. Ryssland håller på att uppgradera sina kärnvapen till nya
            toppmoderna robotar och det är inte orimligt att man i samband med detta också tar fram nya stridsspetsar
            och inte bara bärare. Med tanke på att Ryssland redan övergett ett antal nedrustnings- och fredsavtal,
            åtminstone sex stycken, inklusive avtalet mot markbaserade medeldistansrobotar, så är det inte otänkbart att
            man nu också övergett kärnvapenprovstoppsavtalet. Det handlar i så fall om en underjordisk detonation, då
            den inte detekterats av satelliter. Frågan är också vad för styrka och på vilket djup. Söker man hos USGS
            finns det inga jordbävningar med magnitud 2.5+ detekterade i norra Ryssland tillbaka till november 2016
            annat än en jordbävning utanför Tiksi. Av Sovjetunionens två främsta provplatser är det bara Novaja Semlja
            som är kvar inom den Ryska Federationen. Man gjorde undantaget Novaja Semlja främst sina 1000+
            provsprängingar i andra sovjetrepubliker än Ryssland. Det finns ett omfattande nätverk av 170 seismiska
            detektorer som ska fånga upp kärnvapenprov, samt 80 stationer av den typ som detekterat Jod-131. Även om
            ursprunget för utsläppet av Jod-131 fortfarande är okänt, så gör frånvaron av seimiska utslag det
            osannolikt, men inte omöjligt, att Ryssland brutit mot provstoppet. Dock är Kreml medvetna om de seismiska
            detektorerna, vilket väcker frågan om det alls är möjligt att givet kunskapen ändå kunna göra test med t ex
            taktiska små laddningar, t ex de som ska finnas i markrobotavtalbrytande Iskander-M utan att det detekteras?
            Oavsett finns det någon anledning till att Constant Phoenix ombaserats till Europa. Sannolikt handlar det om
            detekterad Jod-131.
        """,
            "languageCode": "sv",
            "locationCode": "se",
            "links": [
                """
                https://1.bp.blogspot.com/-4uNjjiNQiug/WKguo1sBxwI/AAAAAAAAqKE/_eR7cY8Ft3cd2fYCx-2yXK8AwSHE_A2GgCLcB/s1600/aaea427ee3eaaf8f47d650f48fdf1242.jpg
            """,
                """
                http://www.irsn.fr/EN/newsroom/News/Pages/20170213_Detection-of-radioactive-iodine-at-trace-levels-in-Europe-in-January-2017.aspx
            """,
                "https://www.t.co/2P4IDmovzH",
                "https://www.twitter.com/Strat2Intel/status/832710701730844672"
            ],
            "tags": [
                "Frankrike",
                "försvar",
                "Ryssland",
                "USA",
                "vetenskap"
            ],
            "indexedAt": "2017-02-18T13:12:03Z",
            "publishedAt": "2017-02-18T10:26:00Z",
            "reindexedAt": "2017-02-22T15:58:31Z",
            "inlinksCount": "15",
            "blogId": "12072801357614410355",
            "blogName": "Cornucopia?",
            "blogUrl": "http://cornucopia.cornubot.se",
            "blogRank": "9",
            "authority": "1591"
        })

        self.assert_blog_posts_equal(posts[0], expectedPost)

    def test_valid_coordinates_result(self):
        expected_coordinates = { 'latitude': 49.1, 'longitude': 10.75 }
        data = self.get_fixture("valid_coordinates_result")
        r = twingly_search.Parser().parse(data)
        self.assertIsInstance(r, twingly_search.Result)
        self.assertEqual(r.posts[0].coordinates, expected_coordinates)
        self.assertEqual(r.posts[0].latitude, expected_coordinates.get('latitude'))
        self.assertEqual(r.posts[0].longitude, expected_coordinates.get('longitude'))
