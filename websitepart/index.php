<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Document</title>
</head>
<body>
        <header>
        <h1>Hockey Eerste klasse tussenstand</h1>
    </header>
    <section id="banner">
        <h2>FAIRPLAY</h2>
        <p>De SPORT-bond ziet toe op een eerlijk verloop van de competitie. Onze topsporters dienen een voorbeeld te zijn voor de vele amateurs in de sport. Daarom streven we naar fair play; een sportieve omgang met elkaar. Daar hoort ook bij dat er weinig overtredingen plaatsvinden tijdens een wedstrijd. Op deze website geven we inzicht in het verloop van de competitie tot nu toe. U ziet de wedstrijden met de minste overtredingen, maar voor bewustwording brengen we ook de wedstrijden met de meeste overtredingen in beeld</p>
    </section>
    <section id="features">
        <section id="overtredingcount">
            <div class="totaalovertreding">
                <h3>aantal overtredingen</h3>
                <?php echo file_get_contents ?>
            </div>
            <div class="gemovertreding">
                <h3>gemiddelde overtredingen</h3>
                <?php echo file_get_contents("../pythonpart/data/") ?>
            </div>
        </section>
        <section id="overtredinglist">
            <div class="top5overtreding">
            <h3>de top 5 wedstrijden met de meeste overtredingen</h3>
            </div>
            <div class="last21games">
                <h3>alle wedstrijden van de laatste 21dagen waarin maximaal één overtreding is geweest</h3>
            </div>
        </section>
    </section>
</div>
</body>
</html>