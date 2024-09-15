from io import BytesIO
from pathlib import Path

from weasyprint import HTML
from wand.image import Image
from wand.color import Color



output = (
    Path(__file__).parent
    / 'htmlimage.png')

common = (
    Path(__file__).parent
    / 'static/common.css')

fonts = (
    Path(__file__).parent
    / 'static/fonts.css')

gtaca_file = (
    Path(__file__).parent
    / 'static/gtaca.png')

gtarp_file = (
    Path(__file__).parent
    / 'static/gtarp.png')

gtacash = f'<img src="file://{gtaca_file}">'
gtarp = f'<img src="file://{gtarp_file}">'



html_string = f"""
    <link rel="stylesheet" href="file://{common}">
    <link rel="stylesheet" href="file://{fonts}">

    <table>
     <tbody>
      <tr><td>

        <table class="special">
         <thead>
          <tr>
           <td>2x {gtacash} and {gtarp}</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td>Collection Time Adversary Mode</td>
          </tr>
         </tbody>
        </table>

        <table class="special">
         <thead>
          <tr>
           <td>2x {gtacash}</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td>Salvage Yard Daily Income</td>
          </tr>
         </tbody>
        </table>

        <table class="special">
         <thead>
          <tr>
           <td colspan="2">Free Vehicles</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <th class="center shrink">Casino</td>
           <td>Western Powersurge</td>
          </tr>
          <tr>
            <th class="center shrink">LSCM</td>
            <td>Vapid Peyote Gasser</td>
          </tr>
         </tbody>
        </table>

      </td><td>

        <table class="special">
         <thead>
          <tr>
           <td colspan="2">Vehicle Discounts</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td>Enus Stafford</td>
           <th class="center shrink">30%</td>
          </tr>
          <tr>
            <td>Grotti Stinger</td>
            <th class="center shrink">30%</td>
          </tr>
          <tr>
            <td>Progen Tyrus</td>
            <th class="center shrink">30%</td>
          </tr>
         </tbody>
        </table>

        <table class="special">
         <thead>
          <tr>
           <td colspan="2">Gun Van Discounts</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td>Battle Axe</td>
           <th class="center shrink">40%</td>
          </tr>
          <tr>
            <td>Widowmaker (GTA+)</td>
            <th class="center shrink">40%</td>
          </tr>
         </tbody>
        </table>

        <table class="special">
         <thead>
          <tr>
           <td>Weekly Challenge</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td>Complete a Vehicle Robbery</td>
          </tr>
         </tbody>
        </table>

      </td></tr>
      <tr><td colspan="2">

        <table class="special">
         <thead>
          <tr>
           <td colspan="2">Daily Objectives</td>
          </tr>
         </thead>
         <tbody>
          <tr>
           <td>Monday</td>
           <td>Complete a Dispatch mission.</td>
          </tr>
          <tr>
           <td>Tuesday</td>
           <td>Complete a Diamond Casino Heist Prep.</td>
          </tr>
          <tr>
           <td>Wednesday</td>
           <td>Complete The Diamond Casino Heist Finale.</td>
          </tr>
          <tr>
           <td>Thursday</td>
           <td>Participate in the Transform Series.</td>
          </tr>
          <tr>
           <td>Friday</td>
           <td>Participate in Drop Zone.</td>
          </tr>
          <tr>
           <td>Saturday</td>
           <td>Participate in a Bike Race.</td>
          </tr>
          <tr>
           <td>Sunday</td>
           <td>Participate in a Deathmatch.</td>
          </tr>
         </tbody>
        </table>

      </td></tr>
     </tbody>
    </table>
    """



tempfile = BytesIO()
html = HTML(string=html_string)
html.write_pdf(tempfile)
tempfile.seek(0)



with Image(
    file=tempfile,
    resolution=300
) as img:
    img.trim(Color('transparent'))
    img.format = 'png'
    img.save(filename=str(output))
