text1="Linear regression analysis is used to predictthe value of a variable based on the value ofanother variable. The variable you want topredict is called the dependent variable. Thevariable you are using to predict the othervariable's value is called the independenvariable. This form of analysis estimates the"
text2=" Logistic regression is a supervised machinelearning algorithm widely used for binaryclassification tasks, such as identifyingwhether an email is spam or not and diagnosingdiseases by assessing the presence or absenceof specific conditions based on patient test results. This approach utilizes the logistic"


def motsCommuns(text1,text2):
    L1 = text1.split()
    L2 = text2.split()
    communs_mots = []
    for mot in L1:
        if mot in L2 and len(mot) > 3:
            communs_mots.append(mot)
    return communs_mots

print("La liste des mots avec len sup 3 communs à text1 et text2 est : ",motsCommuns(text1,text2))

