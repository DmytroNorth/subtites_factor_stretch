from datetime import datetime


def subs_factor_stretch(subs, stretch):
    """
    Function to stretch subtitles by a given factor.

    Parameters
    ----------
    subs : str
        Path to the formatted srt subtitles file.
    stretch : float
        The factor by which to stretch the subtitles: 1.04, 1.05, etc.

    Returns
    -------
    None.
        Creates a new file subs_stretched.srt with the stretched subtitles.
    """

    def sub_factor(sub, stretch):
        """
        Function to stretch individual subtitle by a given factor.

        Parameters
        ----------
        sub : str
            The subtitle to stretch: HH:MM:SS,MMM
        stretch : float
            The factor by which to stretch the subtitle: 1.04, 1.05, etc.
        """
        sub = sub.replace(',', '.')  # replacing coma with dot
        # converting to datetime object
        sub = datetime.strptime(sub, '%H:%M:%S.%f')
        sub = sub - datetime(1900, 1, 1)  # converting to seconds
        sub *= stretch  # adjusting the time
        sub = datetime(1900, 1, 1) + sub  # converting back to datetime object
        return sub.strftime('%H:%M:%S,%f')[:-3]  # convert to string

    with open(subs, 'r') as f:
        lines = f.readlines()   # read all lines as a list
    with open('subs_stretched.srt', 'w') as f:  # open new file
        for l in range(len(lines)):  # iterate over lines
            if '-->' in lines[l]:
                # if line contains -->, split it
                subs_line = lines[l].split('-->')
                for i in range(len(subs_line)):      # iterate over the list of 2 subs
                    # apply stretch function to each sub
                    subs_line[i] = sub_factor(subs_line[i].strip(), stretch)
                    # join the list of 2 subs
                    lines[l] = f'{subs_line[0]} --> {subs_line[1]}\n'
            f.write(lines[l])  # write the line to the new file


subs_factor_stretch('subs.srt', 1.0416667)  # call the main function
