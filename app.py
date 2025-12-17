from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, os
from datetime import date

app = Flask(__name__)
app.secret_key = "f1_secret_2025"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "site.db")

# ---------------- DB ----------------
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def calc_age(birth):
    y, m, d = map(int, birth.split("-"))
    today = date.today()
    return today.year - y - ((today.month, today.day) < (m, d))


def init_db():
    db = get_db()
    c = db.cursor()

    # USERS
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)

    # DRIVERS
    c.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            team TEXT,
            nationality TEXT,
            birth_date TEXT,
            points INTEGER,
            titles INTEGER,
            wins INTEGER,
            podiums INTEGER,
            poles INTEGER,
            first_season INTEGER
        )
    """)

    # TEAMS
    c.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            points INTEGER
        )
    """)

    # CIRCUITS
    c.execute("""
        CREATE TABLE IF NOT EXISTS circuits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            country TEXT,
            city TEXT,
            date TEXT,
            description TEXT
        )
    """)

    # LIMPA DADOS ESPORTIVOS
    c.execute("DELETE FROM drivers")
    c.execute("DELETE FROM teams")
    c.execute("DELETE FROM circuits")

    # ===== DRIVERS 2025 (DADOS CONSOLIDADOS F1) =====
    drivers = [
        ("Max Verstappen", "Red Bull Racing", "NED", "1997-09-30", 421, 3, 61, 107, 40, 2015),
        ("Yuki Tsunoda", "Red Bull Racing", "JPN", "2000-05-11", 33, 0, 0, 1, 0, 2021),

        ("Lando Norris", "McLaren", "GBR", "1999-11-13", 423, 1, 7, 18, 7, 2019),
        ("Oscar Piastri", "McLaren", "AUS", "2001-04-06", 410, 0, 2, 11, 0, 2023),

        ("Lewis Hamilton", "Ferrari", "GBR", "1985-01-07", 156, 7, 103, 197, 104, 2007),
        ("Charles Leclerc", "Ferrari", "MON", "1997-10-16", 242, 0, 5, 30, 23, 2018),

        ("George Russell", "Mercedes", "GBR", "1998-02-15", 319, 0, 1, 11, 1, 2019),
        ("Kimi Antonelli", "Mercedes", "ITA", "2006-08-25", 150, 0, 0, 0, 0, 2025),

        ("Fernando Alonso", "Aston Martin", "ESP", "1981-07-29", 56, 2, 32, 106, 22, 2001),
        ("Lance Stroll", "Aston Martin", "CAN", "1998-10-29", 33, 0, 0, 3, 1, 2017),

        ("Carlos Sainz", "Williams", "ESP", "1994-09-01", 64, 0, 3, 21, 3, 2015),
        ("Alexander Albon", "Williams", "THA", "1996-03-23", 73, 0, 0, 2, 0, 2019),

        ("Gabriel Bortoleto", "Kick Sauber", "BRA", "2004-10-14", 19, 0, 0, 0, 0, 2025),
        ("Nico Hulkenberg", "Kick Sauber", "GER", "1987-08-19", 51, 0, 0, 0, 1, 2010),

        ("Pierre Gasly", "Alpine", "FRA", "1996-02-07", 22, 0, 1, 4, 0, 2017),
        ("Franco Colapinto", "Alpine", "ARG", "2003-05-27", 0, 0, 0, 0, 0, 2024),

        ("Esteban Ocon", "Haas F1 Team", "FRA", "1996-09-17", 38, 0, 1, 3, 0, 2016),
        ("Oliver Bearman", "Haas F1 Team", "GBR", "2005-05-08", 41, 0, 0, 0, 0, 2024),

        ("Liam Lawson", "Racing Bulls", "NZL", "2002-02-11", 38, 0, 0, 0, 0, 2023),
        ("Isack Hadjar", "Racing Bulls", "FRA", "2004-09-28", 51, 0, 0, 0, 0, 2025),

        ("Daniel Ricciardo", "Red Bull Racing", "AUS", "1989-07-01", 0, 0, 8, 32, 3, 2011),

    ]

    c.executemany("""
        INSERT INTO drivers
        (name, team, nationality, birth_date, points, titles, wins, podiums, poles, first_season)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, drivers)

    # ===== TEAMS =====
    teams = [
        ("McLaren", 833),
        ("Red Bull Racing", 454),
        ("Ferrari", 398),
        ("Mercedes", 469),
        ("Williams", 137),
        ("Aston Martin", 89),
        ("Kick Sauber", 70)
    ]
    c.executemany("INSERT INTO teams (name, points) VALUES (?, ?)", teams)

    # ===== CIRCUITS 2025 =====
    circuits = [
    ("Bahrain International Circuit", "Bahrein", "Sakhir", "2025-03-02",
     "Circuito moderno e tradicional abertura da temporada."),
    ("Jeddah Corniche Circuit", "Arábia Saudita", "Jeddah", "2025-03-09",
     "Circuito urbano extremamente rápido e técnico."),
    ("Albert Park Circuit", "Austrália", "Melbourne", "2025-03-23",
     "Circuito semiurbano com corridas imprevisíveis."),
    ("Suzuka Circuit", "Japão", "Suzuka", "2025-04-06",
     "Um dos circuitos mais técnicos e respeitados da Fórmula 1."),
    ("Shanghai International Circuit", "China", "Xangai", "2025-04-20",
     "Circuito moderno com longas retas."),
    ("Miami International Autodrome", "Estados Unidos", "Miami", "2025-05-04",
     "Circuito urbano em torno do Hard Rock Stadium."),
    ("Autodromo Enzo e Dino Ferrari", "Itália", "Imola", "2025-05-18",
     "Circuito histórico e técnico."),
    ("Circuit de Monaco", "Mônaco", "Monte Carlo", "2025-05-25",
     "O circuito urbano mais icônico da Fórmula 1."),
    ("Circuit Gilles Villeneuve", "Canadá", "Montreal", "2025-06-08",
     "Conhecido por muros próximos e grandes disputas."),
    ("Circuit de Barcelona-Catalunya", "Espanha", "Barcelona", "2025-06-22",
     "Circuito técnico usado para testes."),
    ("Red Bull Ring", "Áustria", "Spielberg", "2025-06-29",
     "Curto, rápido e intenso."),
    ("Silverstone Circuit", "Reino Unido", "Silverstone", "2025-07-06",
     "Berço da Fórmula 1 moderna."),
    ("Hungaroring", "Hungria", "Budapeste", "2025-07-20",
     "Travado e técnico."),
    ("Circuit de Spa-Francorchamps", "Bélgica", "Spa", "2025-07-27",
     "Um dos circuitos mais lendários da F1."),
    ("Circuit Zandvoort", "Países Baixos", "Zandvoort", "2025-08-24",
     "Rápido e inclinado."),
    ("Autodromo Nazionale di Monza", "Itália", "Monza", "2025-08-31",
     "O templo da velocidade."),
    ("Baku City Circuit", "Azerbaijão", "Baku", "2025-09-14",
     "Urbano com longuíssima reta."),
    ("Marina Bay Street Circuit", "Singapura", "Singapura", "2025-09-21",
     "Corrida noturna extremamente exigente."),
    ("Circuit of the Americas", "Estados Unidos", "Austin", "2025-10-05",
     "Traçado inspirado em circuitos clássicos."),
    ("Autódromo Hermanos Rodríguez", "México", "Cidade do México", "2025-10-26",
     "Circuito em alta altitude."),
    ("Autódromo José Carlos Pace", "Brasil", "São Paulo", "2025-11-09",
     "Interlagos, palco de finais históricos. Dizem que até hoje é possivel ouvir o ronco daquela mclaren mp4/4"),
    ("Las Vegas Street Circuit", "Estados Unidos", "Las Vegas", "2025-11-23",
     "Circuito urbano noturno na Strip."),
    ("Lusail International Circuit", "Catar", "Lusail", "2025-11-30",
     "Circuito moderno e rápido."),
    ("Yas Marina Circuit", "Emirados Árabes Unidos", "Abu Dhabi", "2025-12-07",
     "Tradicional encerramento da temporada.")
]

    c.executemany("""
        INSERT INTO circuits (name, country, city, date, description)
        VALUES (?, ?, ?, ?, ?)
    """, circuits)

    db.commit()
    db.close()


# ---------------- ROUTES ----------------
@app.route("/")
def index():
    db = get_db()
    drivers = db.execute(
        "SELECT name, team, points FROM drivers ORDER BY points DESC LIMIT 5"
    ).fetchall()
    db.close()
    return render_template("index.html", drivers=drivers)


@app.route("/pilotos")
def pilotos():
    db = get_db()
    pilotos = db.execute(
        "SELECT *, birth_date FROM drivers ORDER BY points DESC"
    ).fetchall()
    db.close()

    pilotos = [
        dict(p, age=calc_age(p["birth_date"]))
        for p in pilotos
    ]

    return render_template("pilotos.html", pilotos=pilotos)


@app.route("/piloto/<int:id>")
def driver_detail(id):
    db = get_db()
    p = db.execute("SELECT * FROM drivers WHERE id = ?", (id,)).fetchone()
    db.close()

    if not p:
        return redirect(url_for("pilotos"))

    piloto = dict(p)
    piloto["age"] = calc_age(p["birth_date"])

    return render_template("driver_detail.html", piloto=piloto)


@app.route("/circuitos")
def circuitos():
    db = get_db()
    circuitos = db.execute(
        "SELECT * FROM circuits ORDER BY date ASC"
    ).fetchall()
    db.close()
    return render_template("circuitos.html", circuitos=circuitos)

@app.route("/circuito/<int:id>")
def circuito_detail(id):
    db = get_db()
    circuito = db.execute(
        "SELECT * FROM circuits WHERE id = ?",
        (id,)
    ).fetchone()
    db.close()

    if not circuito:
        return redirect(url_for("circuitos"))

    return render_template("circuito_detail.html", circuito=circuito)

@app.route("/calendario")
def calendario():
    db = get_db()
    races = db.execute(
        "SELECT * FROM circuits ORDER BY date ASC"
    ).fetchall()
    db.close()
    return render_template("calendario.html", races=races)

# -------- EQUIPES --------
@app.route("/equipes")
def equipes():
    db = get_db()
    equipes = db.execute(
        "SELECT * FROM teams ORDER BY points DESC"
    ).fetchall()
    db.close()
    return render_template("equipes.html", equipes=equipes)


@app.route("/equipe/<int:id>")
def equipe_detail(id):
    db = get_db()
    equipe = db.execute(
        "SELECT * FROM teams WHERE id = ?", (id,)
    ).fetchone()

    if not equipe:
        db.close()
        return redirect(url_for("equipes"))

    pilotos = db.execute(
        "SELECT * FROM drivers WHERE team = ? ORDER BY points DESC",
        (equipe["name"],)
    ).fetchall()

    db.close()
    return render_template(
        "equipe_detail.html",
        equipe=equipe,
        pilotos=pilotos
    )


# -------- CLASSIFICAÇÃO --------
@app.route("/classificacao")
def classificacao():
    db = get_db()
    standings = db.execute(
        "SELECT * FROM drivers ORDER BY points DESC"
    ).fetchall()
    db.close()
    return render_template("classificacao.html", standings=standings)


# -------- AUTH --------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE email = ?",
            (request.form["email"],)
        ).fetchone()
        db.close()

        if user and check_password_hash(user["password"], request.form["password"]):
            session["user"] = user["name"]
            flash("Login realizado com sucesso!", "success")
            return redirect(url_for("index"))

        flash("E-mail ou senha inválidos.", "danger")

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                (
                    request.form["name"],
                    request.form["email"],
                    generate_password_hash(request.form["password"])
                )
            )
            db.commit()
            flash("Cadastro realizado com sucesso!", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("E-mail já cadastrado.", "danger")
        finally:
            db.close()

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da conta.", "info")
    return redirect(url_for("index"))

# ---------------- RUN ----------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=8000)
