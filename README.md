<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minhas Skills</title>
    <style>
        body {
            background-color: #001E36;
            color: #FFFFFF;
            font-family: 'Arial', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        h2 {
            margin: 20px 0;
            font-size: 1.8em;
        }
        .skills-container {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin: 20px 0;
        }
        .skill {
            margin: 10px;
            padding: 20px;
            background-color: #242938;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
            transition: transform 0.3s;
            text-align: center;
            width: 150px;
        }
        .skill:hover {
            transform: scale(1.05);
        }
        img {
            width: 80%;
            margin: 0 auto;
        }
        .trophy {
            margin: 20px 0;
            display: flex;
            justify-content: center;
        }
    </style>
</head>
<body>
    <h1>Opa, á todos! Isso é só um belo começo...</h1>
    
    <picture>
        <source
            media="(prefers-color-scheme: dark)"
            srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg"
        />
        <source
            media="(prefers-color-scheme: light)"
            srcset="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg"
        />
        <img
            alt="github contribution grid snake animation"
            src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake.svg"
        />
    </picture>

    <h2>Skills</h2>
    <div class="skills-container">
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=python" alt="Python">
            <p>Python</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=javascript" alt="JavaScript">
            <p>JavaScript</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=html" alt="HTML">
            <p>HTML</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=css" alt="CSS">
            <p>CSS</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=php" alt="PHP">
            <p>PHP</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=java" alt="Java">
            <p>Java</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=sql" alt="SQL">
            <p>SQL</p>
        </div>
        <div class="skill">
            <img src="https://skillicons.dev/icons?i=git" alt="Git">
            <p>Git</p>
        </div>
    </div>

    <p>
        <img align="left" src="https://github-readme-stats.vercel.app/api/top-langs?username=foltzbr&show_icons=true&locale=en&layout=compact&theme=radical" alt="foltzbr" />
        <img align="center" src="https://github-readme-stats.vercel.app/api?username=foltzbr&show_icons=true&locale=en&theme=radical" alt="foltzbr" />
    </p>

    <div class="trophy">
        <img src="https://github-profile-trophy.vercel.app/?username=foltzbr&theme=dracula&row=2&no-bg=true&column=3&margin-w=15&margin-h=15" alt="Trophies" />
    </div>
</body>
</html>
