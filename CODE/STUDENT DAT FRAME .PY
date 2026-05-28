import pandas as pd


class StudentDataFrame(pd.DataFrame):
    """Our custom class that extends pandas DataFrame.

    Adds grade management methods for student data.
    Made by: M.Sami, M.Shziab, M.Dawood
    """

    # ERRORS WE FACED  FIX 1 & 2: Placed inside the class, fixed the smushed import statement,
    # and correctly bound the @property decorator to it.
    @property
    def _constructor(self):
        return StudentDataFrame

    def add_grades(self):
        """New method: Adds a 'grade' column based on marks.

        Uses the inherited .apply() from NDFrame (parent class).
        """
        if "marks" not in self.columns:
            raise ValueError("Need a 'marks' column!")

        def letter_grade(mark):
            if mark >= 85:
                return "A"
            elif mark >= 70:
                return "B"
            elif mark >= 55:
                return "C"
            elif mark >= 40:
                return "D"
            else:
                return "F"

        # .apply() and .copy() are INHERITED from NDFrame
        result = self.copy()
        result["grade"] = result["marks"].apply(letter_grade)
        return result

    def class_stats(self):
        """New method: Returns a simple summary of class performance."""
        if "marks" not in self.columns:
            raise ValueError("Need a 'marks' column!")
        return {
            "Average Marks": round(self["marks"].mean(), 1),
            "Highest Marks": self["marks"].max(),
            "Lowest Marks": self["marks"].min(),
            "Pass Rate": f"{(self['marks'] >= 40).mean()*100:.0f}%",
            "Total Students": len(self),
        }

    def top_students(self, n=3):
        """New method: Returns top n students by marks.

        Uses inherited .nlargest() from NDFrame.
        """
        # FIX 3: Changed 'name' to 'student_name' or fixed the target based on your sample data keys
        return self.nlargest(n, "marks")[["name", "marks"]]


# ── DEMO ──────────────────────────────────────────────────────────
if __name__ == "__main__":

    # Create our custom DataFrame
    sdf = StudentDataFrame(
        {
            "name": ["Sami", "Shziab", "Dawood", "Ali", "Sara", "Zara"],
            "marks": [88, 76, 92, 45, 71, 55],
        }
    )

    print("=" * 40)
    print("  STUDENT GRADE REPORT")
    print("=" * 40)
    print(sdf.add_grades().to_string(index=False))

    print("\n  CLASS STATISTICS:")
    for key, val in sdf.class_stats().items():
        print(f"  {key:20s}: {val}")

    print("\n  TOP 3 STUDENTS:")
    print(sdf.top_students(3).to_string(index=False))
