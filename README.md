Technical documentation for asset creation

How to Install
--------------

1- Download the addon in zip format.
2- Inside of Blender, go to Edit - Preferences - Add-ons ad then click "Install" and look for the zip file you just downloaded. Then tick the box whan it appears.
3- You will find the add-on in the "UA Production Tools" category, in the right part of the viewport.

---------------
Addon Sections:
---------------

*Gender*
--------- 

Choose the gender of your assets:


*Import armature* 
------------------

Import the armature of the avatar. Once you do, you will see the message "Armature is set".


*Add/create garments* 
----------------------

We have 4 different asset types:
Tops: jackets, shirts, jerseys etc.
Bottoms: pants, skirts etc.
Shoes: sneakers, sandals etc.
Accessories: glasses, helmets etc.

IMPORTANT NOTE: Any given outfit can only have one of them at the same time, and cannot have other asset types.

When you import the assets of your outfit to the scene, you will need to select the ones that you want to include.

Once you select the parts you want to include, you will get the "Choose selected object as..." message. 
You just have to select the corresponding object in your scene and press the red button.

Once you have linked the objects, if the material name is different from the object name, you will see the "Rename material" button. Just click the red button to rename the material.

Once you have all the assets with the correct naming and materials, we can continue.


*Parent Garments to armature* 
------------------------------

All the garments should be parented to the Armature. If you see the message "Object X is not parented to the armature" it means that those garments are not parented. Press the Fix button to parent them.


*Apply Transformations* 
------------------------

For an asset to be correct, it has to have the correct origin and scale. This means that all transformations (location, rotation and scale) should be 0. 
If you see the message "Object X has unapplied transformations" it means that the addon has detected an asset that does not have transformations applied. You can see it in the “Item tab” under the Location, Rotation or Scale values.
To fix it, just press the Fix button in the addon.

IMPORTANT NOTE: When you apply transformations, the custom origin and rotations of your asset will be lost. Please make sure you do this step after finishing your garment.


*Pack Textures*
----------------

If you have unpacked textures in the scene, you will see the "UNPACKED IMAGES IN THE SCENE" message.

This means that some of the textures are not included in the blender file and will be lost when sending it. To fix this, go to File - External Data and click Pack Resources.

*Check that textures are smaller than 150kb*
---------------------------------------------

It’s very important to have optimized textures to have a decent sized avatar. If some of your textures are too big, you will see the "Some images are too big" message.

You will have to reduce the image size using an external application (for example: https://squoosh.app/) to meet the requirements. 


*Delete unexpected objects*
----------------------------

If you have extra objects in your scene that are not expected by the addon, you will see the following message:

Unexpected objects in the scene: [Object]. Please remove it

You have to delete all the extra objects in your scene.


*Check polycount*
-----------------

If the outfit is less than 15.000 tris, the addon will inform you it's correct.

If you see the message "Outfit triangle count 16000/15000. Please reduce it to be able to export" it means that you have to reduce your triangle count to fit the limit.


*Check face orientation*
------------------------

The next checks will be confirmed visually. When you activate the Face Orientation Toggle, you will see the faces of your assets either blue or red.

The Blue side is the frontal side. Is the side that should be visible. The red side is the back side, and should not be visible.

If you have some red faces in your assets, you will have to flip the normals of those faces. You can do it by entering edit mode, selecting the red faces, and then going to Mesh - Normals - Flip.


Visible body parts
--------------------

The next step is to select which parts of  the body of the avatar are visible under your assets.

If a body part needs to be visible but your asset collides with it, you will need to adjust your asset.

Once you are satisfied with the result, you should tick the “I have checked  that the visible body parts are correct” Checkbox.


*Rigging & Skinning*
--------------------

For the next step, we will check that the rigging is correct. In the rigging panel you have four poses to check for collisions between assets, collisions between assets and body, and weird stuff in general. 

Please make sure that all four poses work correctly and your character will be ready.


*Deliverable*
-------------

If you did everything right, you should be able to press the “Create GLB and JSON files”.

Once you press it, you will have three files in your blender file folder. A .blend file, a .glb file, and a .json file. These are the files that you have to send with each outfit.

