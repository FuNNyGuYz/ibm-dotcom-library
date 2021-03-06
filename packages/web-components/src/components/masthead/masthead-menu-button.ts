/**
 * @license
 *
 * Copyright IBM Corp. 2020
 *
 * This source code is licensed under the Apache-2.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */

import { property, customElement } from 'lit-element';
import ddsSettings from '@carbon/ibmdotcom-utilities/es/utilities/settings/settings';
import BXHeaderMenuButton from 'carbon-custom-elements/es/components/ui-shell/header-menu-button';
import StableSelectorMixin from '../../globals/mixins/stable-selector';
import styles from './masthead.scss';

const { stablePrefix: ddsPrefix } = ddsSettings;

/**
 * Toggle button for masthead left nav.
 *
 * @element dds-masthead-menu-button
 */
@customElement(`${ddsPrefix}-masthead-menu-button`)
class DDSMastheadMenuButton extends StableSelectorMixin(BXHeaderMenuButton) {
  /**
   * The shadow slot this toggle button should be in.
   */
  @property({ reflect: true })
  slot = 'brand';

  static get stableSelector() {
    return `${ddsPrefix}--masthead__hamburger`;
  }

  static styles = styles; // `styles` here is a `CSSResult` generated by custom WebPack loader
}

export default DDSMastheadMenuButton;
