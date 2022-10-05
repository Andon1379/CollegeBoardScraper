def a(a):
  al = a.split("\n")
  for i in range(len(al)):
    print(str(i) + ") " + al[i])

a("aaaaa")
a("aaaa\naaaa")
a("query courseOutline($subjectId: String, $educationPeriod: String, $filter: String) {\n courseOutline(subjectId: $subjectId, educationPeriod: $educationPeriod, filter: $filter) {\n id: subjectId\n educationPeriod\n ppcTagPair\n subunitLabel\n widgetTagColumn\n widgetTagColumnLabel\n title\n description\n searchResultsTags\n educationPeriod\n unitsLabel\n resources {\n ...resourceFields\n __typename\n }\n units {\n unitId: id\n displayName\n ...n __typename\n }\n ... on AssessmentResource {\n assessmentId\n resourceTypeDetails\n __typename\n }\n ... on StudentPracticeResource {\n assessmentId\n __typename\n }\n ... on GroupResource {\n description\n url\n __typename\n }\n ... on PracticeQuestionsResource {\n questions {\n index\n accNum\n title\n libraryId\n subjectId\n itemId\n hasAllTopicsCovered\n type\n __typename\n }\n __typename\n }\n __typename\n}\n")