# Python ABL Assignment — Flowcharts

This document contains a flowchart for each of the 10 case studies. The diagrams use Mermaid, which GitHub renders directly. The steps stay within the basic Unit I–III topics used by this assignment: input/output, variables, type conversion, arithmetic, conditional statements, loops, strings, lists, tuples and sets.

## 1. Simple Arithmetic Calculator

```mermaid
flowchart TD
    A([Start]) --> B[/Input first number and second number/]
    B --> C[Calculate sum, difference and product]
    C --> D{Second number is zero?}
    D -- Yes --> E[Display division unavailable]
    D -- No --> F[Calculate and display quotient]
    E --> G[Display sum, difference and product]
    F --> G
    G --> H([End])
```

## 2. Student Marks and Grade Calculator

```mermaid
flowchart TD
    A([Start]) --> B[/Input marks/]
    B --> C[Calculate total and average]
    C --> D{Average meets highest grade limit?}
    D -- Yes --> E[Assign highest grade]
    D -- No --> F{Average meets next grade limit?}
    F -- Yes --> G[Assign next grade]
    F -- No --> H{Average meets pass limit?}
    H -- Yes --> I[Assign pass grade]
    H -- No --> J[Assign fail grade]
    E --> K[Display total, average and grade]
    G --> K
    I --> K
    J --> K
    K --> L([End])
```

## 3. Electricity Bill Calculator

```mermaid
flowchart TD
    A([Start]) --> B[/Input units consumed/]
    B --> C{Units are negative?}
    C -- Yes --> D[Display invalid units]
    C -- No --> E[Select applicable unit slab]
    E --> F[Calculate bill using slab rates]
    F --> G[Display bill amount]
    D --> H([End])
    G --> H
```

## 4. Temperature Converter

```mermaid
flowchart TD
    A([Start]) --> B[/Choose conversion direction/]
    B --> C{Celsius to Fahrenheit?}
    C -- Yes --> D[/Input Celsius value/]
    D --> E[ Fahrenheit = Celsius * 9 / 5 + 32 ]
    C -- No --> F[/Input Fahrenheit value/]
    F --> G[ Celsius = (Fahrenheit - 32) * 5 / 9 ]
    E --> H[Display converted temperature]
    G --> H
    H --> I([End])
```

## 5. String Analyzer

```mermaid
flowchart TD
    A([Start]) --> B[/Input a string/]
    B --> C[Find string length]
    C --> D[Convert string to uppercase and lowercase]
    D --> E[Count characters and words as implemented]
    E --> F[Display analysis]
    F --> G([End])
```

## 6. Palindrome Checker

```mermaid
flowchart TD
    A([Start]) --> B[/Input a word or string/]
    B --> C[Compare characters from both ends or compare with reverse]
    C --> D{String is same in reverse?}
    D -- Yes --> E[Display palindrome]
    D -- No --> F[Display not a palindrome]
    E --> G([End])
    F --> G
```

## 7. Star Pattern Generator

```mermaid
flowchart TD
    A([Start]) --> B[/Input number of rows/]
    B --> C[Set row counter to 1]
    C --> D{Row counter <= number of rows?}
    D -- Yes --> E[Print stars for current row]
    E --> F[Move to next line]
    F --> G[Increase row counter]
    G --> D
    D -- No --> H([End])
```

## 8. List Statistics Calculator

```mermaid
flowchart TD
    A([Start]) --> B[/Input list values/]
    B --> C[Set total and count]
    C --> D[Read each list value]
    D --> E[Update total, minimum and maximum]
    E --> F{More values?}
    F -- Yes --> D
    F -- No --> G{Count is greater than zero?}
    G -- Yes --> H[Calculate average]
    G -- No --> I[Display empty-list message]
    H --> J[Display count, sum, minimum, maximum and average]
    I --> K([End])
    J --> K
```

## 9. Student Record Using Tuples

```mermaid
flowchart TD
    A([Start]) --> B[/Input student name, roll number and marks/]
    B --> C[Create tuple with student details]
    C --> D[Unpack tuple values]
    D --> E[Display student record]
    E --> F([End])
```

## 10. Set Operations and Duplicate Removal

```mermaid
flowchart TD
    A([Start]) --> B[/Input values for Set A and Set B/]
    B --> C[Create sets to remove duplicates]
    C --> D[Find union]
    D --> E[Find intersection]
    E --> F[Find difference A minus B]
    F --> G[/Display sets and operation results/]
    G --> H([End])
```

## Notes

- These are algorithm-level flowcharts describing the intended case-study steps.
- Where a project offers fewer options (for example, only one temperature conversion direction), follow the actual program's supported behavior.
- The diagrams describe the logic; they are not evidence that a new execution or screenshot capture was performed.
