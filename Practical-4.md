# Practical 4: GitHub Integration and Branch Management using VS Code

> **Objective (હેતુ):** Visual Studio Code નો ઉપયોગ કરીને Git અને GitHub સેટઅપ કરવું, સ્ટેજ-કમિટ કરવું, GitHub પર કોડ પુશ કરવો અને નવી Branch બનાવવાનું પ્રેક્ટિકલ અમલીકરણ કરવું.

---

## 📋 પૂર્વ-જરૂરિયાતો (Prerequisites)

* **IDE:** Visual Studio Code
* **Version Control System:** Git CLI
* **Account:** GitHub Account

---

## 🛠️ પ્રેક્ટિકલ અમલીકરણ અને પગલાં (Step-by-Step Procedure)

### Step 1: Git Initial Configuration
સૌપ્રથમ VS Code ના ટર્મિનલ (`Ctrl + ~`) માં ગિટમાં મારું નામ અને ઈમેઈલ આઈડી સેટ કર્યું:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
Step 2: VS Code ને GitHub એકાઉન્ટ સાથે Connect કરવું
VS Code ના ડાબા ખૂણે આવેલા Accounts આઈકોન પર ક્લિક કરી Sign in with GitHub પસંદ કર્યું અને બ્રાઉઝરમાં લૉગિન કરી Authorization પરવાનગી આપી.

Step 3: Local Project માં Repository Initialize કરવી
VS Code માં પ્રોજેક્ટ ફોલ્ડર ઓપન કરી ડાબી બાજુની પટ્ટી પરથી Source Control (Ctrl + Shift + G) વિકલ્પમાં જઈને Initialize Repository બટન પર ક્લિક કર્યું.

Step 4: Staging અને Committing Changes
પ્રોજેક્ટની ફાઈલોમાં ફેરફાર કર્યા પછી, Changes સેક્શનમાંથી ફાઈલોને સ્ટેજ કરવા માટે + (Plus) આઈકોન પર ક્લિક કર્યું. ત્યારબાદ કમિટ મેસેજ (દા.ત. Initial Commit) લખીને Commit કર્યું.

Step 5: GitHub પર Repository Publish / Push કરવી
કમિટ પૂર્ણ થયા બાદ Publish Branch બટન પર ક્લિક કર્યું અને રિપોઝિટરીની પ્રાઈવસી (Public/Private) સિલેક્ટ કરી કોડને GitHub પર સફળતાપૂર્વક પુશ કર્યો.

Step 6: નવી Branch બનાવવી અને Switch કરવું
VS Code ના નીચેના Status Bar પર રહેલા બ્રાન્ચના નામ પર ક્લિક કરીને + Create new branch... પસંદ કર્યું અને નવી બ્રાન્ચનું નામ (દા.ત. feature-login) આપીને નવી બ્રાન્ચ પર Switch કર્યું.
