pytest -v -s -m "sanity and regression" --html=Reports\ddtreport.html --browser %browser% testCases/ 
rem pytest -v -s -m "sanity or regression" --html=Reports\ddtreport.html --browser chrome testCases/
rem pytest -v -s -m "sanity" --html=Reports\ddtreport.html --browser chrome testCases/
rem pytest -v -s -m "regression" --html=Reports\ddtreport.html --browser chrome testCases/