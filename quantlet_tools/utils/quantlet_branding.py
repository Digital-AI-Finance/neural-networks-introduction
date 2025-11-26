"""
Quantlet Branding Module

Adds logo, QR code, and clickable URL to matplotlib figures.

Usage:
    from utils.quantlet_branding import add_quantlet_branding

    # At end of chart script, before plt.savefig()
    add_quantlet_branding(fig, chart_url, qr_code_path)
    plt.savefig('chart.pdf')

Configuration:
    Settings are read from utils/branding_config.json
    You can customize logo size, position, colors, etc. in that file.
"""

import json
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def load_config(config_path=None):
    """Load branding configuration from config file."""
    if config_path is None:
        config_path = Path(__file__).parent / 'branding_config.json'
    else:
        config_path = Path(config_path)

    with open(config_path, 'r') as f:
        return json.load(f)


def add_quantlet_branding(fig, chart_url, qr_code_path=None, config_path=None):
    """
    Add Quantlet branding (logo, QR code, URL text) to a matplotlib figure.

    All visual elements are clickable and link to the chart_url.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure to add branding to
    chart_url : str
        The GitHub URL for this chart (used for clickable links)
    qr_code_path : str or Path, optional
        Path to QR code image. If None, looks for 'qr_code.png' in current folder.
    config_path : str or Path, optional
        Custom config file path. If None, uses default branding_config.json.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The figure with branding added

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from utils.quantlet_branding import add_quantlet_branding
    >>>
    >>> fig, ax = plt.subplots()
    >>> ax.plot([1, 2, 3], [4, 5, 6])
    >>> add_quantlet_branding(fig, "https://github.com/user/repo")
    >>> plt.savefig('chart.pdf')
    """
    try:
        # Load configuration
        config = load_config(config_path)

        # Resolve logo path relative to utils folder
        logo_path = Path(__file__).parent / config['logo']['path']

        # Resolve QR code path
        if qr_code_path is None:
            qr_code_path = Path('qr_code.png')
        else:
            qr_code_path = Path(qr_code_path)

        # Add logo with clickable border
        if logo_path.exists():
            logo_img = plt.imread(str(logo_path))
            logo_cfg = config['logo']

            # Apply alpha transparency if specified
            alpha = logo_cfg.get('alpha', 1.0)
            if alpha < 1.0 and logo_img.shape[-1] == 4:  # Has alpha channel
                logo_img = logo_img.astype(float)
                # Normalize to 0-1 range if needed
                if logo_img.max() > 1.0:
                    logo_img = logo_img / 255.0
                logo_img[..., -1] *= alpha

            logo_offset = OffsetImage(logo_img, zoom=logo_cfg['zoom'])

            # Check if frameon is specified in config, default to True for backward compatibility
            frameon = logo_cfg.get('frameon', True)

            logo_box = AnnotationBbox(
                logo_offset,
                tuple(logo_cfg['position']),
                xycoords='figure fraction',
                frameon=frameon,
                box_alignment=(1, 0),
                bboxprops=dict(
                    edgecolor=logo_cfg['border']['color'],
                    linestyle=logo_cfg['border']['linestyle'],
                    linewidth=logo_cfg['border']['linewidth'],
                    alpha=logo_cfg['border']['alpha']
                ) if frameon else None,
                url=chart_url
            )
            fig.add_artist(logo_box)
        else:
            print(f"Warning: Logo not found at {logo_path}")

        # Add QR code (clickable)
        qr_cfg = config['qr_code']
        if qr_cfg['enabled'] and qr_code_path.exists():
            qr_img = plt.imread(str(qr_code_path))

            # Apply alpha transparency if specified
            alpha = qr_cfg.get('alpha', 1.0)
            if alpha < 1.0 and qr_img.shape[-1] == 4:  # Has alpha channel
                qr_img = qr_img.astype(float)
                # Normalize to 0-1 range if needed
                if qr_img.max() > 1.0:
                    qr_img = qr_img / 255.0
                qr_img[..., -1] *= alpha

            qr_offset = OffsetImage(qr_img, zoom=qr_cfg['zoom'])
            qr_box = AnnotationBbox(
                qr_offset,
                tuple(qr_cfg['position']),
                xycoords='figure fraction',
                frameon=False,
                box_alignment=(1, 0),
                url=chart_url
            )
            fig.add_artist(qr_box)

        # Add clickable URL text
        text_cfg = config['url_text']
        if text_cfg['enabled']:
            fig.text(
                text_cfg['position'][0],
                text_cfg['position'][1],
                text_cfg['text'],
                ha='right', va='bottom',
                fontsize=text_cfg['fontsize'],
                color=text_cfg['color'],
                url=chart_url,
                family=text_cfg['family']
            )

        return fig

    except Exception as e:
        print(f"Warning: Could not add Quantlet branding - {e}")
        return fig


if __name__ == "__main__":
    # Test the module
    print("Quantlet Branding Module")
    print("========================")
    print("\nUsage:")
    print("  from utils.quantlet_branding import add_quantlet_branding")
    print("  add_quantlet_branding(fig, chart_url)")
    print("\nConfiguration file: utils/branding_config.json")
