"""Fictional/static math-readiness question bank.

Only public question text/options are returned by the API. Correct option IDs
remain in this server-side module and must never be serialized to the client.
"""
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
    MathQuestion("math-001", "What is 18 + 27?", "arithmetic", "Arithmetic", (("a", "35"), ("b", "45"), ("c", "46"), ("d", "55")), "b", "Add the tens and ones: 18 + 27 = 45."),
    MathQuestion("math-002", "What is 96 ÷ 8?", "arithmetic", "Arithmetic", (("a", "10"), ("b", "11"), ("c", "12"), ("d", "14")), "c", "Because 8 × 12 = 96, the quotient is 12."),
    MathQuestion("math-003", "What is 3/4 + 1/8?", "fractions-decimals", "Fractions and decimals", (("a", "4/12"), ("b", "5/8"), ("c", "7/8"), ("d", "1")), "c", "Convert 3/4 to 6/8, then add 1/8 to get 7/8."),
    MathQuestion("math-004", "What is 0.6 × 0.5?", "fractions-decimals", "Fractions and decimals", (("a", "0.03"), ("b", "0.3"), ("c", "3"), ("d", "1.1")), "b", "Six tenths multiplied by five tenths is thirty hundredths, or 0.3."),
    MathQuestion("math-005", "Solve: 3x + 5 = 20.", "algebra", "Algebra", (("a", "3"), ("b", "5"), ("c", "7"), ("d", "15")), "b", "Subtract 5 from both sides to get 3x = 15, so x = 5."),
    MathQuestion("math-006", "Solve: 2(x − 3) = 14.", "algebra", "Algebra", (("a", "4"), ("b", "7"), ("c", "10"), ("d", "17")), "c", "Divide by 2 to get x − 3 = 7, then add 3 to get x = 10."),
    MathQuestion("math-007", "A rectangle is 8 cm long and 5 cm wide. What is its perimeter?", "geometry", "Geometry", (("a", "13 cm"), ("b", "26 cm"), ("c", "40 cm"), ("d", "80 cm")), "b", "Perimeter = 2 × (length + width) = 2 × (8 + 5) = 26 cm."),
    MathQuestion("math-008", "Two angles of a triangle are 65° and 45°. What is the third angle?", "geometry", "Geometry", (("a", "60°"), ("b", "65°"), ("c", "70°"), ("d", "80°")), "c", "Triangle angles total 180°; 180 − 65 − 45 = 70°."),
    MathQuestion("math-009", "The ratio of red to blue marbles is 2:3. There are 25 marbles altogether. How many are red?", "ratios", "Ratios and proportions", (("a", "5"), ("b", "10"), ("c", "15"), ("d", "20")), "b", "There are 5 equal parts; each part is 25 ÷ 5 = 5, so red marbles = 2 × 5 = 10."),
    MathQuestion("math-010", "A map scale is 1:50,000. What real distance does 4 cm on the map represent?", "ratios", "Ratios and proportions", (("a", "200 m"), ("b", "500 m"), ("c", "2 km"), ("d", "20 km")), "c", "4 × 50,000 cm = 200,000 cm = 2 km."),
    MathQuestion("math-011", "What is the mean of 4, 6, 8 and 10?", "data-interpretation", "Data interpretation", (("a", "6"), ("b", "7"), ("c", "8"), ("d", "9")), "b", "The sum is 28; divide by 4 values to get a mean of 7."),
    MathQuestion("math-012", "A club recorded 12 sign-ups on Monday, 15 on Tuesday and 9 on Wednesday. Which day had the most sign-ups?", "data-interpretation", "Data interpretation", (("a", "Monday"), ("b", "Tuesday"), ("c", "Wednesday"), ("d", "All equal")), "b", "Tuesday had 15 sign-ups, more than Monday's 12 and Wednesday's 9."),
)

ASSESSMENT_ID = "math-readiness-v1"
DURATION_SECONDS = 600
