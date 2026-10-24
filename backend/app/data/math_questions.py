"""Static practice question bank; answer keys remain server-side."""
from dataclasses import dataclass

@dataclass(frozen=True)
class MathQuestion:
    id: str
    prompt: str
    topic: str
    topic_label: str
    options: tuple[tuple[str, str], ...]
    correct_option_id: str
    explanation: str

QUESTION_BANK: tuple[MathQuestion, ...] = (
    MathQuestion("math-001", "What is 18 + 27?", "arithmetic", "Arithmetic", (("a","35"),("b","45"),("c","46"),("d","55")), "b", "18 + 27 = 45."),
    MathQuestion("math-002", "What is 96 ÷ 8?", "arithmetic", "Arithmetic", (("a","10"),("b","11"),("c","12"),("d","14")), "c", "96 divided by 8 is 12."),
    MathQuestion("math-003", "What is 3/4 + 1/8?", "fractions-decimals", "Fractions and decimals", (("a","4/12"),("b","5/8"),("c","7/8"),("d","1")), "c", "3/4 + 1/8 = 7/8."),
    MathQuestion("math-004", "What is 0.6 × 0.5?", "fractions-decimals", "Fractions and decimals", (("a","0.03"),("b","0.3"),("c","3"),("d","1.1")), "b", "0.6 × 0.5 = 0.3."),
    MathQuestion("math-005", "Solve: 3x + 5 = 20.", "algebra", "Algebra", (("a","3"),("b","5"),("c","7"),("d","15")), "b", "x = 5."),
    MathQuestion("math-006", "Solve: 2(x − 3) = 14.", "algebra", "Algebra", (("a","4"),("b","7"),("c","10"),("d","17")), "c", "x = 10."),
    MathQuestion("math-007", "A rectangle is 8 cm long and 5 cm wide. What is its perimeter?", "geometry", "Geometry", (("a","13 cm"),("b","26 cm"),("c","40 cm"),("d","80 cm")), "b", "Perimeter is 26 cm."),
    MathQuestion("math-008", "Two angles of a triangle are 65° and 45°. What is the third angle?", "geometry", "Geometry", (("a","60°"),("b","65°"),("c","70°"),("d","80°")), "c", "The third angle is 70°."),
    MathQuestion("math-009", "The ratio of red to blue marbles is 2:3. There are 25 marbles altogether. How many are red?", "ratios", "Ratios and proportions", (("a","5"),("b","10"),("c","15"),("d","20")), "b", "There are 10 red marbles."),
    MathQuestion("math-010", "A map scale is 1:50,000. What real distance does 4 cm on the map represent?", "ratios", "Ratios and proportions", (("a","200 m"),("b","500 m"),("c","2 km"),("d","20 km")), "c", "The real distance is 2 km."),
    MathQuestion("math-011", "What is the mean of 4, 6, 8 and 10?", "data-interpretation", "Data interpretation", (("a","6"),("b","7"),("c","8"),("d","9")), "b", "The mean is 7."),
    MathQuestion("math-012", "A club recorded 12 sign-ups on Monday, 15 on Tuesday and 9 on Wednesday. Which day had the most sign-ups?", "data-interpretation", "Data interpretation", (("a","Monday"),("b","Tuesday"),("c","Wednesday"),("d","All equal")), "b", "Tuesday had the most sign-ups."),
)
ASSESSMENT_ID = "math-readiness-v1"
DURATION_SECONDS = 600
