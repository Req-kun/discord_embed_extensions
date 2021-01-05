import discord

def make(*, title:str=None, description:str=None, url:str=None, color:int=None, footer:dict=None, image:str=None, thumbnail:str=None, author:dict=None, fields:list=None):
    embed = discord.Embed()
    if title != None:
        embed.title = title
    if description != None:
        embed.description = description
    if url != None:
        embed.url = url
    if color != None:
        embed.colour = color
    if footer != None:
        '''
        footer = {'text': 'text', 'icon_url': 'icon_url'}
        '''
        if 'text' in footer.keys() and 'icon_url' in footer.keys():
            embed.set_footer(text=footer['text'], icon_url=footer['icon_url'])
        if 'text' not in footer.keys() and 'icon_url' in footer.keys():
            embed.set_footer(icon_url=footer['icon_url'])
        if 'text' in footer.keys() and 'icon_url' not in footer.keys():
            embed.set_footer(text=footer['text'])
    if image != None:
        embed.set_image(url=image)
    if thumbnail != None:
        embed.set_thumbnail(url=thumbnail)
    if author != None:
        '''
        author = {'name': 'name', 'url': 'url', 'icon_url': 'icon_url'}
        '''
        # name, url, icon_url
        if 'name' in author.keys() and 'url' in author.keys() and 'icon_url' in author.keys():
            embed.set_author(name=author['name'], url=author['url'], icon_url=author['icon_url'])
        # name, url
        if 'name' in author.keys() and 'url' in author.keys() and 'icon_url' not in author.keys():
            embed.set_author(name=author['name'], url=author['url'])
        # name, icon_url
        if 'name' in author.keys() and 'url' not in author.keys() and 'icon_url' in author.keys():
            embed.set_author(name=author['name'], icon_url=author['icon_url'])
        # name
        if 'name' in author.keys() and 'url' not in author.keys() and 'icon_url' not in author.keys():
            embed.set_author(name=author['name'])
        # url, icon_url
        if 'name' not in author.keys() and 'url' in author.keys() and 'icon_url' in author.keys():
            embed.set_author(url=author['url'], icon_url=author['icon_url'])
        # icon_url
        if 'name' not in author.keys() and 'url' not in author.keys() and 'icon_url' in author.keys():
            embed.set_author(icon_url=author['icon_url'])
        # url
        if 'name' not in author.keys() and 'url' in author.keys() and 'icon_url' not in author.keys():
            embed.set_author(url=author['url'])
    if fields != None:
        '''
        fields = [{'name': 'name', 'value': 'value', 'inline': True / False}, {'name': 'name', 'value': 'value', 'inline': True / False}]
        '''
        for f in fields:
            # name, value, inline
            if 'name' in f.keys() and 'value' in f.keys() and 'inline' in f.keys():
                embed.add_field(name=f['name'], value=f['value'], inline=f['inline'])
            # name
            if 'name' in f.keys() and 'value' not in f.keys() and 'inline' not in f.keys():
                embed.add_field(name=f['name'])
            # value
            if 'name' not in f.keys() and 'value' in f.keys() and 'inline' not in f.keys():
                embed.add_field(value=f['value'])
            # inline
            if 'name' not in f.keys() and 'value' not in f.keys() and 'inline' in f.keys():
                embed.add_field(inline=f['inline'])
            # name, value
            if 'name' in f.keys() and 'value' in f.keys() and 'inline' not in f.keys():
                embed.add_field(name=f['name'], value=f['value'])
            # name, inline
            if 'name' in f.keys() and 'value' not in f.keys() and 'inline' in f.keys():
                embed.add_field(name=f['name'], inline=f['inline'])
            # value, inline
            if 'name' not in f.keys() and 'value' in f.keys() and 'inline' in f.keys():
                embed.add_field(value=f['value'], inline=f['inline'])


    return embed

'''Example

embed = make(
title='title',
description='description',
color=0x00ffff,
url='url',
footer={
    'text': 'footer_text',
    'icon_url': 'footer_icon_url'
},
image=image_url,
thumbnail=image_url,
author={
    'name': 'author_name',
    'url': 'author_url',
    'icon_url': 'author_icon_url'
},
fields=[
    {
        'name': 'field_one_name',
        'value': 'field_one_value'
    },
    {
        'name': 'field_two_name',
        'value': 'field_two_value',
        'inline': False
    }
]
)

'''
