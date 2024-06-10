import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
train = pd.read_csv("https://raw.githubusercontent.com/developer-sdk/kaggle-python-beginner/master/datas/kaggle-titanic/train.csv")

# 교차도표 생성
cross_tab = pd.crosstab(train['Sex'], train['Survived'])

# 교차도표 출력
print(cross_tab)

# 교차도표 시각화
cross_tab.plot(kind='bar', stacked=True)
plt.title('Survival by Gender')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Survived', loc='upper right', labels=['Dead', 'Alive'])
plt.show()