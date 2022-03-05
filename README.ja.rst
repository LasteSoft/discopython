discopython
==========

.. image:: https://discord.com/api/guilds/898698330618613850/embed.png
   :target: https://discord.gg/T6Tz4wZkfE
   :alt: Discordサーバーの招待
.. image:: https://img.shields.io/pypi/v/discopython.svg
   :target: https://pypi.python.org/pypi/discopython
   :alt: PyPIのバージョン情報
.. image:: https://img.shields.io/pypi/pyversions/discopython.svg
   :target: https://pypi.python.org/pypi/discopython
   :alt: PyPIのサポートしているPythonのバージョン
.. image:: https://static.pepy.tech/badge/discopython
   :target: https://pepy.tech/project/discopython
   :alt: 合計ダウンロード数   

discopython は機能豊富かつモダンで使いやすい、非同期処理にも対応したDiscord用のAPIラッパーです。

主な特徴
-------------

- ``async`` と ``await`` を使ったモダンなPythonらしいAPI。
- 適切なレート制限処理
- メモリと速度の両方を最適化。

インストール
-------------

**Python 3.8 以降のバージョンが必須です**

完全な音声サポートなしでライブラリをインストールする場合は次のコマンドを実行してください:

.. code:: sh

    # Linux/OS X
    python3 -m pip install -U discopython

    # Windows
    py -3 -m pip install -U discopython

音声サポートが必要なら、次のコマンドを実行しましょう:

.. code:: sh

    # Linux/OS X
    python3 -m pip install -U discopython[voice]

    # Windows
    py -3 -m pip install -U discopython[voice]


開発版をインストールしたいのならば、次の手順に従ってください:

.. code:: sh

    $ git clone https://github.com/LasteSoft/discopython
    $ cd discopython
    $ python3 -m pip install -U .[voice]


オプションパッケージ
~~~~~~~~~~~~~~~~~~~~~~

* PyNaCl (音声サポート用)

Linuxで音声サポートを導入するには、前述のコマンドを実行する前にお気に入りのパッケージマネージャー(例えば ``apt`` や ``dnf`` など)を使って以下のパッケージをインストールする必要があります:

* libffi-dev (システムによっては ``libffi-devel``)
* python-dev (例えばPython 3.6用の ``python3.6-dev``)

簡単な例
--------------

.. code:: py

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('token')

Botの例
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='>')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

examplesディレクトリに更に多くのサンプルがあります。

リンク
------

- `ドキュメント <https://discopython.readthedocs.io/en/latest/index.html>`_
- `公式Discordサーバー <https://discord.gg/nXzj3dg>`_
- `Discord API <https://discord.com/invite/T6Tz4wZkfE>`_
