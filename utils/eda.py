import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from typing import Optional, List


def missing_values(df: pd.DataFrame) -> pd.DataFrame:
    length = df.shape[0]
    missing_values_count = df.isnull().sum()
    missing_values_percentage = round((df.isnull().sum() / len(df)) * 100, 2)
    summary_df = pd.DataFrame({
        'Missing Values': missing_values_count,
        'Percentage Missing': missing_values_percentage,
        'Datatype': df.dtypes
    })
    return summary_df

def violin_boxplot(data: pd.DataFrame, columns: List[str], title: Optional[
    str] = None, ax=None) -> None:

    if ax is None:
        ax = plt.gca()

    sns.violinplot(data=data[columns], orient='h',
                   density_norm='count', inner=None, ax=ax)
    sns.boxplot(data=data[columns], width=0.2,
                showfliers=True,
                boxprops={'facecolor': 'None'}, orient='h', ax=ax)
    if title:
        ax.set_title(title)


def violin_box_subplots(data: pd.DataFrame, columns: List[str], title:
Optional[str] = None, nrows: int = 1, ncols: int = 1, xlim: Optional[tuple] = None) -> None:
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 5,
                                                                nrows * 4))
    fig.subplots_adjust(hspace=1, wspace=0.4)

    if np.ndim(axes) == 0:
        axes_flatten = [axes]
    else:
        axes_flatten = axes.flatten()

    col_len = len(columns)
    df_len = data.shape[0]
    axes_len = len(axes_flatten)

    for i, column in enumerate(columns):
        sns.violinplot(data=data[columns], orient='h',
                       density_norm='count', inner=None, ax=axes_flatten[i])
        sns.boxplot(data=data[columns], width=0.2,
                    showfliers=True,
                    boxprops={'facecolor': 'None'}, orient='h', ax=axes_flatten[i])

        if xlim:
            axes_flatten[i].set_xlim(xlim)

    if col_len < axes_len:
        for j in range(col_len, len(axes_flatten)):
            axes_flatten[j].clear()
            axes_flatten[j].axis('off')

    if title:
        plt.suptitle(title, fontsize=15)
    plt.tight_layout()
    plt.show()


def count_subplots(data: pd.DataFrame, columns:List[str], title: Optional[
    str] =
None, nrows: int = 1, ncols: int = 1) -> None:

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 5,
                                                                nrows * 4))
    fig.subplots_adjust(hspace=1, wspace=0.4)

    if np.ndim(axes) == 0:
        axes_flatten = [axes]
    else:
        axes_flatten = axes.flatten()

    col_len = len(columns)
    df_len = data.shape[0]
    axes_len = len(axes_flatten)

    for i, col in enumerate(columns):
        sns.countplot(data=data, x=col, ax=axes_flatten[i])
        axes_flatten[i].set_title(col, pad=15)
        for p in axes_flatten[i].patches:
            (axes_flatten[i]
             .annotate(f'{int(p.get_height())}',
                       (p.get_x() + p.get_width() / 2., p
                        .get_height()), ha='center',
                       va='center', xytext=(0, 10),
                       textcoords='offset points'))
        sns.despine(top=True, right=True, left=True, bottom=True)
        axes_flatten[i].tick_params(axis='x', which='both', length=0,
                                    labelbottom=True)
        axes_flatten[i].tick_params(axis='y', which='both', length=0,
                                    labelleft=False)
        axes_flatten[i].set(ylabel=None, xlabel=None)


    if col_len < axes_len:
        for j in range(col_len, len(axes_flatten)):
            axes_flatten[j].clear()
            axes_flatten[j].axis('off')

    if title:
        plt.suptitle(title, fontsize=15)
    plt.tight_layout()
    plt.show()


def percentage_plots(data: pd.DataFrame, columns: List[str], title: Optional[
    str] = None, ax=None) -> None:

    df_len = data.shape[0]
    if ax is None:
        ax = plt.gca()

    sns.countplot(data=data, y=columns, ax=ax, orient='h')  #
    # Horizontal plot
    for p in ax.patches:
        percentage = round((p.get_width() * 100 / df_len), 2)
        (ax
            .annotate(f'{percentage}%',
                   (p.get_width(), p.get_y() + p.get_height() / 2.),
                   ha='center', va='center', xytext=(10, 0),
                   textcoords='offset points'))
    sns.despine(top=True, right=True, left=True, bottom=True)
    ax.tick_params(axis='y', which='both', length=0, labelleft=True)
    ax.tick_params(axis='x', which='both', length=0, labelbottom=False)
    ax.set(ylabel=None, xlabel=None)

    if title:
        ax.set_title(title)

    plt.show()

def percentage_subplots(data: pd.DataFrame, columns: List[str], title: Optional[
    str] = None, nrows: int = 1, ncols: int = 1) -> None:

    # Adjust the height based on the number of rows
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(ncols * 3,
                                                                nrows * 3))
    fig.subplots_adjust(hspace=1, wspace=0.4)

    if np.ndim(axes) == 0:
        axes_flatten = [axes]
    else:
        axes_flatten = axes.flatten()

    col_len = len(columns)
    df_len = data.shape[0]
    axes_len = len(axes_flatten)

    for i, col in enumerate(columns):
        order = data[col].value_counts().sort_values(ascending=False).index
        sns.countplot(data=data, y=col, ax=axes_flatten[i], orient='h', order=order)  # Horizontal plot
        axes_flatten[i].set_title(col, pad=15)
        for p in axes_flatten[i].patches:
            percentage = round((p.get_width() * 100 / df_len), 2)
            (axes_flatten[i]
             .annotate(f'{percentage}%',
                       (p.get_width(), p.get_y() + p.get_height() / 2.),
                       ha='center', va='center', xytext=(10, 0),
                       textcoords='offset points'))
        sns.despine(top=True, right=True, left=True, bottom=True)
        axes_flatten[i].tick_params(axis='y', which='both', length=0, labelleft=True)
        axes_flatten[i].tick_params(axis='x', which='both', length=0, labelbottom=False)
        axes_flatten[i].set(ylabel=None, xlabel=None)

    if col_len < axes_len:
        for j in range(col_len, len(axes_flatten)):
            axes_flatten[j].clear()
            axes_flatten[j].axis('off')

    if title:
        plt.suptitle(title, fontsize=15)
    plt.tight_layout()
    plt.show()


def stacked_bar_plot(df: pd.DataFrame, col: str, hue: str,
                     color: Optional[List[str]] = None,
                     title: Optional[str] = None, xlabel: Optional[str] = None,
                     ylabel: Optional[str] = None, ax: Optional[plt.Axes] =
                     None) -> None:
    """
    Plots a stacked bar chart with the given DataFrame and column,
    with stack segments defined by hue.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data_csv.
        col (str): The column name to be used as the x-axis.
        hue (str): The column name used to define the stack segments.
        color (Optional[List[str]]): A list of colors for each stack segment.
        title (Optional[str]): The title of the plot.
        xlabel (Optional[str]): The label for the x-axis.
        ylabel (Optional[str]): The label for the y-axis.

    """
    categories = df[col].unique()
    hues = df[hue].unique()

    if color is None:
        color = sns.color_palette('dark', n_colors=len(hues))

    if ax is None:
        fig, ax = plt.subplots()

    bottom = np.zeros(len(categories))

    for idx, h in enumerate(hues):
        group_data = df[df[hue] == h].groupby(col).size().reindex(categories, fill_value=0)
        ax.bar(categories, group_data, bottom=bottom, color=color[idx], label=h)
        bottom += group_data.values

    ax.set_xlabel(xlabel if xlabel else col)
    ax.set_ylabel(ylabel if ylabel else 'Count')
    ax.set_title(title if title else f'{col} Counts by {hue}')
    ax.legend(title=hue, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.show()

def stacked_bar_by_segment(data: pd.DataFrame, col: List[str], segment_col:
str = 'Segment', ax=None, title: Optional[str] = None, palette: Optional[
    dict[str, str]] = None) -> None:

    if ax is None:
        fig, ax = plt.subplots()

    ct = pd.crosstab(data[segment_col], data[col], normalize='index') * 100
    ct = ct.sort_index()  # Ensure segments are in consistent order

        # Plot stacked horizontal bars
    left = np.zeros(len(ct))
    for i, category in enumerate(ct.columns):
        color = palette.get(category, None) if palette else None
        ax.barh(ct.index, ct[category], left=left, label=category, color=color)
        left += ct[category]

    ax.set_title(title if title else 'Distribution of Responses by Segment')
    ax.set_xlabel('Percentage')
    ax.set_ylabel('Segment')
    ax.set_xlim(0, 100)
    plt.show()

from typing import Optional, Dict
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def stacked_bar_by_segment(data: pd.DataFrame, feature: str, segment_col: str = 'Segment',
                           figsize: tuple = (8, 5), ax=None, title:
        Optional[str] = None, palette: Optional[Dict[str, str]] = None) -> None:
    """
    Plots a horizontal stacked bar chart for one categorical feature,
    showing the distribution of responses by segment.
    """
    # Prepare the normalized crosstab
    ct = pd.crosstab(data[segment_col], data[feature], normalize='index') * 100
    ct = ct.sort_index()

    # Set up the plot
    if ax is None:
        fig, ax = plt.subplots(figsize=figsize)
    left = np.zeros(len(ct))

    for category in ct.columns:
        color = palette.get(category) if palette else None
        ax.barh(ct.index, ct[category], left=left, label=category, color=color)
        left += ct[category]

    ax.set_xlabel('Percentage')
    ax.set_ylabel(segment_col)
    ax.set_xlim(0, 100)
    ax.set_title(title if title else f'Distribution of {feature} by {segment_col}')
    ax.legend(title=feature, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()



def stacked_horizontal_feature_distribution(data: pd.DataFrame, columns:
List[str], title: Optional[str] = None, figsize: tuple = (10, 10)) -> None:

    missing_columns = [col for col in columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"The following columns are not in the DataFrame: {missing_columns}")

    percentages = {}
    for feature in columns:
        percentages[feature] = data[feature].value_counts(normalize=True)

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

    fig, ax = plt.subplots(figsize=figsize)

    for i, feature in enumerate(columns):
        left = 0
        for j, (category, value) in enumerate(percentages[feature].items()):
            if (value > 0.12):
                ax.barh(i, value * 100, left=left, color=colors[j % len(colors)])
                text_val = f'{category}\n{value * 100:.2f}%' if value*100 < 200 \
                    else ''
                ax.text(left + value * 100 / 2, i,
                        text_val,
                        ha='center', va='center', color='black', fontsize=10)

                left += value * 100
            else:
                ax.barh(i, value * 100, left=left, color=colors[j % len(colors)])
                text_val = ''
                ax.text(left + value * 100 / 2, i,
                        text_val,
                        ha='center', va='center', color='black', fontsize=7)

                left += value * 100

    ax.set_yticks(np.arange(len(columns)))
    ax.set_yticklabels(columns)

    ax.set_xlabel('Percentage')
    ax.set_title(title)

    # Display the plot
    plt.tight_layout()
    plt.show()


def horizontal_binary_distribution(data: pd.DataFrame, columns:
List[str], title: Optional[str] = None, figsize: tuple = (10, 10)) -> None:
    # Check for missing columns
    missing_columns = [col for col in columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"The following columns are not in the DataFrame: {missing_columns}")

    # Calculate percentages
    percentages = {}
    for feature in columns:
        percentages[feature] = data[feature].value_counts(normalize=True)

    # Sort by the percentage of 0 in descending order
    sorted_columns = sorted(columns, key=lambda col: percentages[col].get(0, 0), reverse=True)

    # Define colors for 0 and 1
    colors = ['#66b3ff', '#ff9999']  # 0 = blue, 1 = red

    # Create the plot
    fig, ax = plt.subplots(figsize=figsize)
    for i, feature in enumerate(sorted_columns):
        left = 0
        for j, value in enumerate([percentages[feature].get(0, 0), percentages[feature].get(1, 0)]):
            # Plot the bar
            ax.barh(i, value * 100, left=left, color=colors[j])

            # Add the percentage text
            ax.text(left + value * 100 / 2, i, f'{value * 100:.1f}%',
                    ha='center', va='center', color='black', fontsize=10)
            left += value * 100

    # Add labels and titles
    ax.set_yticks(np.arange(len(sorted_columns)))
    ax.set_yticklabels(sorted_columns)
    ax.set_xlabel('Percentage')
    ax.set_title(title if title else 'Feature Distribution')

    # Add legend for 0 and 1
    ax.legend(['0', '1'], loc='upper right', title='Category')

    # Display the plot
    plt.tight_layout()
    plt.show()
