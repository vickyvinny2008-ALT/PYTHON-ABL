# Python ABL Assignment — Test Cases

These test cases are designed for the 10 beginner Python projects in this repository. Run each program with the listed input and compare its output with the expected result. For interactive programs, prompts may appear before the result.

> **Status:** Test cases documented for manual verification. Results have not been marked as passed because automated execution of the repository programs has not been performed here.

## 1. Simple Arithmetic Calculator
| ID | Test input | Expected result |
|---|---|---|
| CALC-01 | First number: 10; second number: 5 | Addition 15, subtraction 5, multiplication 50, division 2 |
| CALC-02 | First number: 7; second number: 0 | Division-by-zero is handled safely; other operations remain correct |
| CALC-03 | First number: -4; second number: 2 | Addition -2, subtraction -6, multiplication -8, division -2 |

## 2. Student Grade Calculator
| ID | Test input | Expected result |
|---|---|---|
| GRADE-01 | Marks: 90, 80, 70 | Average 80; grade matches the program's documented grading scale |
| GRADE-02 | All marks: 0 | Average 0; lowest grade/fail result according to the grading scale |
| GRADE-03 | Any mark below 0 or above 100 | Invalid marks are rejected or clearly flagged, if validation is implemented |

## 3. Electricity Bill Calculator
| ID | Test input | Expected result |
|---|---|---|
| BILL-01 | Units consumed: 0 | Bill is 0 or the documented minimum charge |
| BILL-02 | Units consumed: 100 | Bill follows the program's stated unit-rate/slab calculation |
| BILL-03 | Units consumed: 250 | Higher-use calculation follows the stated slab/rate rules |

## 4. Temperature Converter
| ID | Test input | Expected result |
|---|---|---|
| TEMP-01 | Celsius: 0 | Fahrenheit 32 |
| TEMP-02 | Celsius: 100 | Fahrenheit 212 |
| TEMP-03 | Fahrenheit: 32 | Celsius 0 (if Fahrenheit-to-Celsius conversion is supported) |

## 5. String Analyzer
| ID | Test input | Expected result |
|---|---|---|
| STR-01 | `Hello World` | Length 11; character/word counts match the documented behavior |
| STR-02 | Empty string | Handles empty input without crashing; length 0 |
| STR-03 | `Python` | Uppercase `PYTHON` and lowercase `python` where those operations are provided |

## 6. Palindrome Checker
| ID | Test input | Expected result |
|---|---|---|
| PAL-01 | `madam` | Identified as a palindrome |
| PAL-02 | `python` | Identified as not a palindrome |
| PAL-03 | `level` | Identified as a palindrome |

## 7. Star Pattern Generator
| ID | Test input | Expected result |
|---|---|---|
| PAT-01 | Rows: 1 | One row containing one star |
| PAT-02 | Rows: 3 | Three rows in the selected pattern; star counts follow the pattern |
| PAT-03 | Rows: 5 | Five rows in the selected pattern; alignment and row count are correct |

## 8. List Statistics
| ID | Test input | Expected result |
|---|---|---|
| LIST-01 | List: 1, 2, 3, 4, 5 | Count 5, minimum 1, maximum 5, sum 15, average 3 |
| LIST-02 | List: -2, 0, 2 | Count 3, minimum -2, maximum 2, sum 0, average 0 |
| LIST-03 | List: 4, 4, 4 | Count 3, minimum 4, maximum 4, sum 12, average 4 |

## 9. Student Record Using Tuples
| ID | Test input | Expected result |
|---|---|---|
| TUP-01 | Name: Asha; roll number: 12; marks: 85 | Tuple/record displays the supplied values correctly |
| TUP-02 | Name containing a space, e.g. `Ravi Kumar` | Full name is retained as entered |
| TUP-03 | Numeric roll number and marks | Values are stored/displayed in the intended types and order |

## 10. Set Operations
| ID | Test input | Expected result |
|---|---|---|
| SET-01 | Set A: 1, 2, 3; Set B: 3, 4, 5 | Union {1, 2, 3, 4, 5}; intersection {3}; difference A−B {1, 2} |
| SET-02 | Input contains duplicates: 1, 1, 2, 2, 3 | Set contains unique values {1, 2, 3} |
| SET-03 | Two disjoint sets: {1, 2} and {3, 4} | Intersection is empty |

## General checks
- Run each project with valid input and confirm it completes without an exception.
- Where relevant, test zero, negative values, empty input, and boundary values.
- Python sets do not guarantee a display order; compare set membership rather than printed order.
- For grade and electricity calculations, use the exact thresholds and rates documented in the corresponding project README.
- Record actual results and mark each case PASS/FAIL after running the program locally.

## How to run
From the repository root, run a project using its folder path, for example:

```bash
python 01_Simple_Calculator/main.py
```

Repeat with the relevant folder for each of the other projects.

## Execution results (2026-10-29)

The 20 checks below were executed against the current `main.py` program logic using scripted input and captured output. **20 passed, 0 failed.** These are smoke tests for representative valid and invalid inputs, not exhaustive testing.

| Project | Test cases run | Result |
|---|---:|---|
| 01 Simple Calculator | Addition; division by zero | 2/2 PASS |
| 02 Student Grade Calculator | Average/grade B; marks above 100 | 2/2 PASS |
| 03 Electricity Bill Calculator | 100-unit bill; negative units | 2/2 PASS |
| 04 Temperature Converter | 0°C to 32°F; 32°F to 0°C | 2/2 PASS |
| 05 String Analyzer | Text with digits; empty string | 2/2 PASS |
| 06 Palindrome Checker | Palindrome; non-palindrome | 2/2 PASS |
| 07 Star Pattern Generator | 3-row pattern; zero rows | 2/2 PASS |
| 08 List Statistics | Values 1–5; zero count | 2/2 PASS |
| 09 Student Record Using Tuples | Passing record; failing record with a spaced name | 2/2 PASS |
| 10 Set Operations | Union/intersection/difference and membership present/absent | 2/2 PASS |
| **Total** | **20** | **20 PASS, 0 FAIL** |

### Important notes
- The scripts were run with representative test inputs and their printed output was checked against expected output.
- Set display order can vary in Python; compare the set's values rather than relying on printed ordering.
- These results verify the current program logic for the listed cases only. Invalid non-numeric input and other unlisted edge cases have not all been tested.

