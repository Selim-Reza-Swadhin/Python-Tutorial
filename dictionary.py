studentId = {
    "101": "Anisul Islam",
    "102": "Selim",
    "103": "Reza",
    104: "Swadhin"
}

print(studentId["101"])
print(studentId[104])
# print(studentId["106"])
print(studentId.get("106"))
print(studentId.get("106", "Not a valid key"))
print(studentId.get("103", "Not a valid key"))
