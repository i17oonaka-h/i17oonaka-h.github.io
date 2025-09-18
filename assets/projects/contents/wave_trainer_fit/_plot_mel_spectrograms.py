import matplotlib.pyplot as plt
import json
import argparse
from pathlib import Path
import json
import seaborn as sns
import seaborn.objects as so
import pandas as pd
import torchaudio
import torch

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['mathtext.fontset'] = 'stix'
# ticks in
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

expr_dir = Path("./")
fig_save_path = Path("./imgs/")
fig_save_path.mkdir(parents=True, exist_ok=True)

wavs_pattern = "5105_28241_000027_000002_*.wav"

cm = 1/2.54  # centimeters to inches conversion factor
scale = 2. # scale factor for figure size

mel = torchaudio.transforms.MelSpectrogram(
    sample_rate=24000,
    n_fft=2048,
    win_length=2048,
    hop_length=128,
    n_mels=128,
    f_min=20,
    f_max=12000,
    power=2,
    norm='slaney',
    mel_scale='htk'
)

waves = sorted(expr_dir.glob(wavs_pattern))
print(waves)

for wav_path in waves:
    fig, ax = plt.subplots(1, 1, figsize=(8.6*cm*scale, 2*cm*scale))  # 8.6 cm width, 4 cm height
    fig.set_facecolor('#e9e8dc')
    ax.tick_params(pad=1, labelsize=4*scale)
    ax: plt.Axes
    # load wav file
    wav, sr = torchaudio.load(str(wav_path))
    mel_spec = mel(wav)
    mel_spec_db = 10 * torch.log10(mel_spec + 1e-10)
    t = torch.arange(mel_spec_db.shape[-1]) * 128 / sr
    f = torch.arange(0, 128)
    f_plot = torch.tensor([128, 512, 1024, 2048, 4096, 8192, 12000]) # [Hz]
    mel_bin = 2595 * torch.log10(1 + f_plot / 700)
    mel_max = 2595 * torch.log10(1 + torch.tensor([12000]) / 700)
    mel_bin = mel_bin / mel_max * 128
    f_plot = f_plot.tolist()

    ax.pcolormesh(t, f, mel_spec_db[0], vmax=20, vmin=-80)
    ax.set_xlabel("Time [s]", fontsize=8*scale)
    ax.set_ylabel("Frequency [Hz]", fontsize=8*scale)
    tshow = ax.get_xticks()
    ax.set_xticks(tshow)
    ax.set_xticklabels([f"{t:.1f}" for t in tshow], fontsize=6*scale)
    ax.set_xlim([0, t.max()])
    ax.set_yticks(mel_bin.tolist())
    ax.set_yticklabels([str(f_hz) for f_hz in f_plot], fontsize=6*scale)
    ax.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.5)
    cbar = fig.colorbar(ax.collections[0], ax=ax, format    ='%+2.0f dB')
    cbar.ax.tick_params(labelsize=4*scale)
    stem = wav_path.stem
    fig.savefig(fig_save_path / f"{stem}.png", dpi=300, bbox_inches='tight')
    # fig.savefig(fig_save_path / f"{stem}.pdf", dpi=300, bbox_inches='tight')
    plt.close(fig)

