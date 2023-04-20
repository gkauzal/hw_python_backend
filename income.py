import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from flask import Flask
from flask import send_file

app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
    #data_source = np.random.randint(1, 6, 40).reshape(10, 4)
    # your code goes here....
    with open('income.txt', 'r') as f:
        lines = f.readlines()[1:]  # skip first line (header)
        data_source = []
        for line in lines:
            line = line.strip()
            values = line.split(',')
            values = [int(val.replace(' ', '')) for val in values]
            data_source.append(values)
    df = pd.DataFrame(data_source)
    df.columns = ['Class A', 'Class B', 'Class C', 'Class D']
    sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
    sns_plot.figure.savefig("output.png")
    plt.close()
    return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)