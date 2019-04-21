# A Death by the Data
A *Song of Ice and Fire* data visualization exploring the relationships between death, gender, social class, and literary structure.
![alt text](https://i.imgur.com/JRGKOvk.jpg "A Death by the Data")

## Technologies used
* [Django-ChartJS](https://github.com/peopledoc/django-chartjs) (an extension of [Chart.js](https://www.chartjs.org/))
* Django
* PostgreSQL
* HTML
* CSS

## Deployed with
* Heroku (front end)
* ElephantSQL

While the database itself is not publicly accessible, you can view my data in [Google Sheets](https://docs.google.com/spreadsheets/d/1apfpE1Rd8Ae7KLWHUk54y1p0e76DTkmdVYligH0kR-c/edit?usp=sharing).

## Development Process

### First Normal Form
**Characters**

| Name (PK)        | House    | Gender | Manner of Death | Book of Death       | Chapter of Death |
|------------------|----------|--------|-----------------|---------------------|------------------|
| Dalla            |          | Female | Childbirth      | "A Storm of Swords" | 76               |
| Bran Stark       | Stark    | Male   |                 |                     |                  |
| Torrhen Karstark | Karstark | Male   | Asphyxiation    | "A Game of Thrones" | 63               |


### Second Normal Form
**Characters**

| Character ID | Name             | Gender |
|--------------|------------------|--------|
| 1            | Dalla            | Female |
| 2            | Bran Stark       | Male   |
| 3            | Torrhen Karstark | Male   |

**Books**

| Book ID | Title                |
|---------|----------------------|
| 1       | A Game of Thrones    |
| 2       | A Clash of Kings     |
| 3       | A Storm of Swords    |
| 4       | A Feast for Crows    |
| 5       | A Dance with Dragons |

**Nobility**

| Character ID | House    |
|--------------|----------|
| 2            | Stark    |
| 3            | Karstark |

**Manner of Death**

| Character ID | Manner of Death |
|--------------|-----------------|
| 1            | Childbirth      |
| 3            | Asphyxiation    |

**Book/Chapter of Death**

| Character ID | Book of Death ID | Chapter of Death |
|--------------|------------------|------------------|
| 1            | 3                | 76               |
| 3            | 1                | 63               |

### Third Normal Form
**Characters** (no changes)

| Character ID | Book of Death ID | Chapter of Death |
|--------------|------------------|------------------|
| 1            | 3                | 76               |
| 3            | 1                | 63               |

**Books** (no changes)

| Book ID | Title                |
|---------|----------------------|
| 1       | A Game of Thrones    |
| 2       | A Clash of Kings     |
| 3       | A Storm of Swords    |
| 4       | A Feast for Crows    |
| 5       | A Dance with Dragons |

**Nobility** (no changes)

| Character ID | House    |
|--------------|----------|
| 2            | Stark    |
| 3            | Karstark |

**Manner of Death** (no changes)

| Character ID | Manner of Death |
|--------------|-----------------|
| 1            | Childbirth      |
| 3            | Asphyxiation    |

**Book of Death**

| Character ID | Book of Death ID |
|--------------|------------------|
| 1            | 3                |
| 3            | 1                |

**Chapter of Death**

| Character ID | Chapter of Death |
|--------------|------------------|
| 1            | 76               |
| 3            | 63               |


## Acknowledgements
* Thank you to Myles O'Neill for putting together the original dataset from which this project was derived. You can download the original CSV, "character-deaths.csv", on [Kaggle](https://www.kaggle.com/mylesoneill/game-of-thrones)
* Additionally, thanks go out to Erin Pierce and Ben Kahle for collecting the data for that spreadsheet as part of their [Bayesian survival analysis](http://allendowney.blogspot.com/2015/03/bayesian-survival-analysis-for-game-of.html) of the series.
* Shoutout to literally every contributor at [A Wiki of Ice and Fire](https://awoiaf.westeros.org/index.php/Main_Page) for all of their efforts cateloguing such an expansive mass of data. I heavily used this as a resource to confirm methods of death for each character.
* Thank you George R. R. Martin for creating this series in the first place! Please finish *The Winds of Winter* now.
* Finally, thank you to my General Assembly Software Engineering Immersive instructors, [Zakk Fleischmann](https://github.com/ZakkMan) and [Hammad Malik](https://github.com/tomatohammado) for your continuing support and encouragement. Y'all sure have taught me a thing or two or ten thousand.