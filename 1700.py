class Solution:
    def countStudents(self, students, sandwiches):
        c1, c0 = students.count(1), students.count(0)
        for i in  sandwiches:
            if i == 0:
                if c0 > 0:
                    c0 -= 1
                else:
                    break
            elif i == 1:
                if c1 > 0:
                    c1 -= 1
                else:
                    break
        return c0 + c1